package com.example.firstandroidapp;

import androidx.appcompat.app.AppCompatActivity;

import android.os.Bundle;
import android.util.Log;
import android.widget.TextView;

import com.github.angads25.toggle.interfaces.OnToggledListener;
import com.github.angads25.toggle.model.ToggleableView;
import com.github.angads25.toggle.widget.LabeledSwitch;

import org.eclipse.paho.client.mqttv3.IMqttDeliveryToken;
import org.eclipse.paho.client.mqttv3.MqttCallbackExtended;
import org.eclipse.paho.client.mqttv3.MqttException;
import org.eclipse.paho.client.mqttv3.MqttMessage;

import java.nio.charset.Charset;

public class MainActivity extends AppCompatActivity
{
    MQTTHelper mqttHelper;
    TextView txtTemp, txtHumid;
    LabeledSwitch buttonLed1, buttonLed2;
    @Override
    protected void onCreate(Bundle savedInstanceState)
    {
        super.onCreate(savedInstanceState);
        setContentView(R.layout.activity_main);

        txtTemp = findViewById(R.id.txtTemperature);
        txtHumid = findViewById(R.id.txtHumidity);
        buttonLed1 = findViewById(R.id.buttonLed1);
        buttonLed2 = findViewById(R.id.buttonLed2);

        // from mobile to adafruit
        buttonLed1.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn)
            {
                if(isOn == true)
                {
                    sendDataMQTT("Nhat_Tien_2002/feeds/button-1", "1");
                }
                else
                {
                    sendDataMQTT("Nhat_Tien_2002/feeds/button-1", "0");
                }
            }
        });

        buttonLed2.setOnToggledListener(new OnToggledListener() {
            @Override
            public void onSwitched(ToggleableView toggleableView, boolean isOn)
            {
                if(isOn == true)
                {
                    sendDataMQTT("Nhat_Tien_2002/feeds/button-2", "1");
                }
                else
                {
                    sendDataMQTT("Nhat_Tien_2002/feeds/button-2", "0");
                }
            }
        });

        startMQTT();
    }

    public void sendDataMQTT(String topic, String value)
    {
        MqttMessage msg = new MqttMessage();
        msg.setId(1234);
        msg.setQos(0);
        msg.setRetained(false);

        byte[] b = value.getBytes(Charset.forName("UTF-8"));
        msg.setPayload(b);

        try {
            mqttHelper.mqttAndroidClient.publish(topic, msg);
        }catch (MqttException e){
        }
    }

    public void startMQTT()
    {
        mqttHelper = new MQTTHelper(this);
        mqttHelper.setCallback(new MqttCallbackExtended() {
            @Override
            public void connectComplete(boolean reconnect, String serverURI) {

            }

            @Override
            public void connectionLost(Throwable cause) {

            }

            // from adafruit to mobile
            @Override
            public void messageArrived(String topic, MqttMessage message) throws Exception {
                Log.d("TEST", topic + "***" + message.toString());
                if(topic.contains("sensor-1"))
                {
                    txtTemp.setText(message.toString() + "°C");
                }
                else if(topic.contains("sensor-2"))
                {
                    txtHumid.setText(message.toString() + "%");
                }
                else if(topic.contains("button-1"))
                {
                    if(message.toString().equals("1"))
                    {
                        buttonLed1.setOn(true);
                    }
                    else
                    {
                        buttonLed1.setOn(false);
                    }
                }
                else if(topic.contains("button-2"))
                {
                    if(message.toString().equals("1"))
                    {
                        buttonLed2.setOn(true);
                    }
                    else
                    {
                        buttonLed2.setOn(false);
                    }
                }
            }

            @Override
            public void deliveryComplete(IMqttDeliveryToken token) {

            }
        });
    }
}