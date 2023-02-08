/* MagicMirror² Config Sample
 *
 * By Michael Teeuw https://michaelteeuw.nl
 * MIT Licensed.
 *
 * For more information on how you can configure this file
 * see https://docs.magicmirror.builders/configuration/introduction.html
 * and https://docs.magicmirror.builders/modules/configuration.html
 */
let config = {
	address: "localhost", 	// Address to listen on, can be:
							// - "localhost", "127.0.0.1", "::1" to listen on loopback interface
							// - another specific IPv4/6 to listen on a specific interface
							// - "0.0.0.0", "::" to listen on any interface
							// Default, when address config is left out or empty, is "localhost"
	port: 8080,
	basePath: "/", 	// The URL path where MagicMirror² is hosted. If you are using a Reverse proxy
					// you must set the sub path here. basePath must end with a /
	ipWhitelist: ["127.0.0.1", "::ffff:127.0.0.1", "::1",], 	// Set [] to allow all IP addresses
															// or add a specific IPv4 of 192.168.1.5 :
															// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.1.5"],
															// or IPv4 range of 192.168.3.0 --> 192.168.3.15 use CIDR format :
															// ["127.0.0.1", "::ffff:127.0.0.1", "::1", "::ffff:192.168.3.0/28"],

	useHttps: false, 		// Support HTTPS or not, default "false" will use HTTP
	httpsPrivateKey: "", 	// HTTPS private key path, only require when useHttps is true
	httpsCertificate: "", 	// HTTPS Certificate path, only require when useHttps is true

	language: "en",
	locale: "en-US",
	logLevel: ["INFO", "LOG", "WARN", "ERROR"], // Add "DEBUG" for even more logging
	timeFormat: 12,
	units: "imperial",
	// serverOnly:  true/false/"local" ,
	// local for armv6l processors, default
	//   starts serveronly and then starts chrome browser
	// false, default for all NON-armv6l devices
	// true, force serveronly mode, because you want to.. no UI on this device

	modules: [
		{
			module: "alert",

		},
		{
			module: "updatenotification",
			position: "top_bar"
		},
		{
			module: "clock",
			position: "top_left"
		},
		{
			module: "calendar",
			header: "David's Calendar",
			position: "top_left",
			config: {
				fetchInterval: 1000,
				calendars: [
					/*
					{
						symbol: "calendar-check",
						url: "webcal://www.calendarlabs.com/ical-calendar/ics/76/US_Holidays.ics"
					},
					
					{
						symbol: "Your Calendar",
						url: "Use google calendar's secret address in iCal Format"
					},
					*/
				]
			}
		},
		{
			module: "compliments",
			position: "lower_third",
			config: {
				compliments: {
					day_sunny: [
						"Everyday is a good day but today shines brighter than others",
						"Don't forget sunscreen"
					],
					snow: [
						"It never snows here"
					],
					rain: [
						"Don't forget an umbrella",
						"Stay dry"
					],
					morning: [
						"Good morning",
						"How was your sleep?",
						"Have a nice day"
					],
					afternoon: [
						"Good afternoon",
						"I hope you didn't just wake up"
					],
					evening: [
						"What's for dinner?",
						"Good evening"
					],
					"....-01-01": [
						"Happy New Year"
					],
					"....-12-25": [
						"Merry Christmas"
					]
				},
			},
		},
		// {
		// 	module: "weather",
		// 	position: "top_right",
		// 	config: {
		// 		weatherProvider: "openweathermap",
		// 		type: "current",
		// 		location: "Los Angeles",
		// 		locationID: "5368361", //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
		// 		apiKey: "a70ad777aaaa27c1dc13b9a5baf4dc9c"
		// 	}
		// },
		{
			module: "weather",
			position: "top_right",
			header: "Weather Forecast",
			config: {
				colored: true,
				weatherProvider: "openweathermap",
				type: "forecast",
				location: "Los Angeles",
				locationID: "5368361", //ID from http://bulk.openweathermap.org/sample/city.list.json.gz; unzip the gz file and find your city
				apiKey: "a70ad777aaaa27c1dc13b9a5baf4dc9c"
			}
		},
		{
			module: "newsfeed",
			position: "bottom_bar",
			config: {
				feeds: [
					{
						title: "New York Times",
						url: "https://rss.nytimes.com/services/xml/rss/nyt/HomePage.xml"
					}
				],
				showSourceTitle: true,
				showPublishDate: true,
				broadcastNewsFeeds: true,
				broadcastNewsUpdates: true
			}
		},
		{
			module: "MMM-Spotify",
			position: "bottom_left", // "bottom_bar" or "top_bar" for miniBar
			config: {
			  debug: true, // debug mode
			  style: "default", // "default" or "mini" available (inactive for miniBar)
			  moduleWidth: 250, // width of the module in px
			  control: "default", // "default" or "hidden"
			  showAlbumLabel: true, // if you want to show the label for the current song album
			  showVolumeLabel: true, // if you want to show the label for the current volume
			  showAccountName: false, // also show the current account name in the device label; usefull for multi account setup
			  //showAccountButton: true, // if you want to show the "switch account" control button
			  showDeviceButton: true, // if you want to show the "switch device" control button
			  useExternalModal: false, // if you want to use MMM-Modal for account and device popup selection instead of the build-in one (which is restricted to the album image size)
			  updateInterval: 1000, // update interval when playing
			  idleInterval: 30000, // update interval on idle
			  defaultAccount: 0, // default account number, attention : 0 is the first account
			  defaultDevice: null, // optional - if you want the "SPOTIFY_PLAY" notification to also work from "idle" status, you have to define your default device here (by name)
			  allowDevices: [], //If you want to limit devices to display info, use this. f.e. allowDevices: ["RASPOTIFY", "My Home speaker"],
			  
			  //   null, // disable onStart feature with `null`
			  // if you want to start playback of song
			  
			  // if you want to send custom notifications when suspending the module, f.e. switch MMM-Touch to a different "mode"
			  notificationsOnSuspend: [
				{
				  notification: "TOUCH_SET_MODE",
				  payload: "myNormalMode",

				},
				{
				  notification: "WHATEVERYOUWANT",
				  payload: "sendMe",
				},
			  ],
			  // if you want to send custom notifications when resuming the module, f.e. switch MMM-Touch to a different "mode"
			  notificationsOnResume: [
				{
				  notification: "TOUCH_SET_MODE",
				  payload: "mySpotifyControlMode",
				},
			  ],
			  deviceDisplay: "Listening on", // text to display in the device block (default style only)
			  volumeSteps: 5, // in percent, the steps you want to increase or decrese volume when reacting on the "SPOTIFY_VOLUME_{UP,DOWN}" notifications
			  // miniBar is no longer supported, use at your own "risk". Will be removed in a future version
			  miniBarConfig: {
				album: true, // display Album name in miniBar style
				scroll: true, // scroll title / artist / album in miniBar style
				logo: true, // display Spotify logo in miniBar style
			  }
			}
		},

		{
			module: "MMM-NotificationReceived",
			disabled: false,
			config: {
			  notificationFrom : [ "MMM-Spotify", "calendar" ]
			}
	    },

		{
			module: 'MMM-SmartTouch', 
			position: 'bottom_center',    // This can be any of the regions.(bottom-center Recommended)
			config:{ 
			  // None configuration options defined 
			}
		},

		{
			module:"MMM-VoiceControl",
			position:"center",
			disabled:false,
			config: {
				// name of the python process to execute (could be python3)
				pythonName: 'python3',
				// command file in module folder
				// if false, YOU will provide the full path to the python program
				localfolder: true,
	   
				// spawn a python pgm that writes over and over (timed maybe), but keeps running
				command: 'wake.py',
				repetative: true,
	   
				// spawn a one time output  script, but relaunch it every cycletime milliseconds
	   
				// repretative: false,
				// command: 'printitonce.py',
				// cycletime: 2000,   // only used in repetative:false
	   
				// print debugging messages from the node_helper
				debug: true
			}
		},
	]
};



/*************** DO NOT EDIT THE LINE BELOW ***************/
if (typeof module !== "undefined") {module.exports = config;}
