import 'react-native-gesture-handler'
import * as React from 'react';
import {useState} from 'react';

// React Navigator
import { NavigationContainer, } from '@react-navigation/native'
import { createStackNavigator, } from '@react-navigation/stack'

// Native components
import { 
  Image, 
  SafeAreaView, 
  ScrollView, 
  StyleSheet, 
  Switch,
  Text, 
  TextInput, 
  TouchableOpacity, 
  View, 
} from 'react-native'

// Custom components
//import Form from './src/components/Form'

const LoginScreen = () => {
  return (
    <View style={styles.form}>
        <TextInput style={styles.textinput} placeholder="Email"
        underlineColorAndroid={'transparent'} />

        <TextInput style={styles.textinput} placeholder="Password"
        secureTextEntry={true} underlineColorAndroid={'transparent'} />

        <TouchableOpacity style={styles.button}>
            <Text style={styles.btntext}>Log In</Text>
        </TouchableOpacity>
    </View>
  );
};


const SignUpScreen = () => {
  return (
    <View style={styles.form}>
        <Text style={styles.header}>Register</Text>
        
        <TextInput style={styles.textinput} placeholder="Full name"
        underlineColorAndroid={'transparent'} />
        
        <TextInput style={styles.textinput} placeholder="Email"
        underlineColorAndroid={'transparent'} />

        <TextInput style={styles.textinput} placeholder="Password"
        secureTextEntry={true} underlineColorAndroid={'transparent'} />

        <TouchableOpacity style={styles.button}>
            <Text style={styles.btntext}>Sign Up</Text>
        </TouchableOpacity>
    </View>
  );
};

const HomeScreen = ({ navigation }) => {
  return (
    <View style={{ flex: 1, alignItems: 'center', justifyContent: 'center', backgroundColor: '#293e66', }}>
      <TouchableOpacity 
        style={styles.button}
        onPress={() => navigation.navigate('Login')}
      >
        <Text style={styles.btntext}>Log In</Text>
      </TouchableOpacity>
      <TouchableOpacity 
        style={styles.button}
        onPress={() => navigation.navigate('Register')}
      >
        <Text style={styles.btntext}>Register</Text>
      </TouchableOpacity>
      <TouchableOpacity 
        style={styles.button}
        onPress={() => navigation.navigate('Profile')}
      >
        <Text style={styles.btntext}>Profile</Text>
      </TouchableOpacity>
      <TouchableOpacity 
        style={styles.button}
        onPress={() => navigation.navigate('About')}
      >
        <Text style={styles.btntext}>About</Text>
      </TouchableOpacity>
    </View>
  );
};

const ProfileScreen = () => {
  const [isEnabled, setIsEnabled] = useState(false);
  const toggleSwitch = () => setIsEnabled(previousState => !previousState);
  
  return (
    <View style={{ flex: 1, alignItems: 'center', backgroundColor: '#293e66' }}>
      <Image 
        style={{ marginTop: 10, width: 250, height: 100, }}
        source={require('./assets/logo.png')}
      />
      <Text style={{ fontSize: 28, color: '#fff', padding: 10, marginTop: 10, }}>Jon Doe</Text>
      <Text style={{ fontSize: 20, color: '#fff', padding: 10, }}>Occupation: Job Seeker</Text>
      <View style={{ flexDirection: 'row'}}>
        <Text style={{ color: '#fff', }}>Looking for Employment?</Text>
        <Switch
          trackColor={{false: '#767577', true: '#81b0ff'}}
          thumbColor={isEnabled ? '#f5dd4b' : '#f4f3f4'}
          ios_backgroundColor='#3e3e3e'
          onValueChange={toggleSwitch}
          value={isEnabled}
        />
      </View>
    </View>
  );
};

const AboutScreen = () => {
  return (
    <SafeAreaView>
      <ScrollView>
        <View style={{ flexHorizontal: 1, alignItems: 'center', backgroundColor: '#293e66' }}>
          <Text style={{ color: '#fff', marginTop: 10, marginLeft: 10, marginRight: 10, fontSize: 20, fontWeight: "bold", justifyContent: 'center', }}>
            About Us
          </Text>
          <Image
            style={{ marginTop: 10, width: 250, height: 100, }}
            source={require('./assets/logo.png')}
          />
          <Text style={{ fontWeight: 'bold', color: '#fff', marginLeft: 10, marginRight: 10, marginBottom: 10, textAlign: 'center'}}>
            {'\n'}
            The business was the ‘light bulb’ moment that was born out of the 
            tiresome process of job searching. The amount of time away from family 
            and loved ones creating profiles and populating the exact same 
            monotonous information on various platforms was exhausting, 
            emotionally draining, and extremely frustrating.
            {'\n\n'}
            We created this platform for those people who are experiencing the same 
            frustrations who understand and appreciate that time is their most 
            valuable and important commodity and should spend it doing things that 
            really matter to them.
            {'\n\n'}
            There had to be an easier way! Welcome to eeZIPEEzii, the online 
            platform that does it all for you. You spend your time doing what is 
            important to you and we spend our time looking for work for you.
            {'\n\n'}
            At eeZIPEEzii, our aim is to empower candidates looking to secure 
            employment by making their job search experience as simple and 
            effective as possible whilst maximizing opportunity. Therefore, we want 
            to put our users’ best foot forward for any role they apply for and 
            this is why we feel it paramount that we pre-qualify and authenticate 
            our users by doing all due diligence and background checks before 
            rather than after. Once authentication has been complete, eeZIPEEzii 
            provides its clients with a user-friendly platform that enables them to 
            search the internet, through specific user-defined parameters, for all 
            available positions. eeZIPEEzii’s unique structure and supporting 
            software empower the user by giving them the ability to access more 
            sites, apply for more roles in less time, and increase their probability 
            of success... AND only populating their profile ONCE!
            {'\n\n'}
            Our clients would be anyone, on any level, from any background, 
            anywhere, looking to secure work. Our system is able to perform this 
            function for the user in a fraction of the time whilst being able to 
            provide feedback to our client through data analytics.
            {'\n\n'}
            At eeZIPEEzii, our aim is to empower candidates looking to secure 
            employment by making their job search experience as simple and effective 
            as possible whilst maximizing opportunity. Therefore, we want to put our 
            users’ best foot forward for any role they apply for and this is why we 
            feel it paramount that we pre-qualify and authenticate our users by 
            doing all due diligence and background checks before rather than after. 
            Once authentication has been complete, eeZIPEEzii provides its clients 
            with a user-friendly platform that enables them to search the internet, 
            through specific user-defined parameters, for all available positions. 
            eeZIPEEzii’s unique structure and supporting software empower the user 
            by giving them the ability to access more sites, apply for more roles 
            in less time, and increase their probability of success... AND only 
            populating their profile ONCE!
            {'\n\n'}
            eeZIPEEzii, Jobs in a ZIPEE, life made eezii.
          </Text>
        </View>
      </ScrollView>
    </SafeAreaView>
  );
};

const Stack = createStackNavigator();

const App = () => {
  return (
    <NavigationContainer>
      <Stack.Navigator>
        <Stack.Screen
          name="Home"
          component={HomeScreen}
          options={{title: 'eeZIPEEzii' }}
        />
        <Stack.Screen
          name="Profile"
          component={ProfileScreen}
          options={{title: 'Profile' }}
        />
        <Stack.Screen
          name="About"
          component={AboutScreen}
          options={{title: 'About eeZIPEEzii' }}
        />
        <Stack.Screen
          name="Register"
          component={SignUpScreen}
          options={{title: 'Create Account' }}
        />
        <Stack.Screen
          name="Login"
          component={LoginScreen}
          options={{title: 'Log In to Your Account' }}
        />
      </Stack.Navigator>
    </NavigationContainer>
  );
}

const styles = StyleSheet.create({
  form: {
    flex: 1,
    alignSelf: 'stretch',
    justifyContent: 'center',
    backgroundColor: '#293e66',
  },
  header: {
      fontSize: 24,
      color: '#fff',
      paddingBottom: 10,
      marginBottom: 40,
      borderBottomColor: '#199187',
      borderBottomWidth: 1,
      textAlign: 'center',
  },
  textinput: {
      alignSelf: 'stretch',
      textAlign: 'center',
      height: 40,
      marginBottom: 30,
      backgroundColor: '#fff',
      borderBottomColor: '#f8f8f8',
      borderBottomWidth: 1,
  }, 
  button: {
      alignSelf: 'stretch',
      alignItems: 'center',
      padding: 20,
      backgroundColor: '#59cbbd',
      marginTop: 30,
  },
  btntext: {
      color: '#fff',
      fontWeight: 'bold',
  },
});

export default App;