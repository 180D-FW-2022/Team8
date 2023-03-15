/*

sample module structure


 */


Module.register("MMM-VoiceControl", {


	// anything here in defaults will be added to the config data
	// and replaced if the same thing is provided in config
	defaults: {
		command: "",
		repetative: true,
		cycletime:0,
		localfolder:false,
		pythonName:"python",
		debug:false
	},

	init: function(){
		Log.log(this.name + " is in init!");
	},

	start: function(){
		Log.log(this.name + " is starting!");
		if(this.config.command == "")
			this.config.command=this.file("wake.py")
	},



	// messages received from other modules and the system (NOT from your node helper)
	// payload is a notification dependent data structure
	notificationReceived: function(notification, payload, sender) {
		// once everybody is loaded up
		if(notification==="ALL_MODULES_STARTED"){
			// send our config to our node_helper
			this.sendSocketNotification("CONFIG",this.config)
		}


	},

	// messages received from from your node helper (NOT other modules or the system)
	// payload is a notification dependent data structure, up to you to design between module and node_helper
	socketNotificationReceived: function(notification, payload) {
		Log.log(this.name + " received a socket notification: " + notification + " - Payload: " + payload);
		if(notification === "WAKE_DETECTED"){
			this.config.message = payload;
			command = parseInt(payload,10);
			console.log("payload = ", command);
			console.log(typeof(command));
			if(command == 1){
				console.log("we want to play a song");
				this.sendNotification("SPOTIFY_TOGGLE");
			}
			if(command == 2){
				console.log("we want to pause this song");
				this.sendNotification("SPOTIFY_PAUSE");
			}
			if(command == 3){
				console.log("skip song");
				this.sendNotification("SPOTIFY_NEXT");
			}
			if(command == 4){
				console.log("go back");
				this.sendNotification("SPOTIFY_PREVIOUS")
			}
			if(command == 6){
				console.log("switching user");
				this.sendNotification("LEAVE_HIDDEN_PAGE");
			}
			if(command == 8 || command == 7){
				console.log("adding a user");
				this.sendNotification("NEW_USER");
				this.sendNotification("SHOW_HIDDEN_PAGE", "spotify");
			}
			if(command == 32){
				console.log("command not understood");
			}
			// if(command == 2)
			// 	console.log("we want to pause the song");
			// 	this.sendNotification("SPOTIFY_PAUSE");
			// if(command == 3)
			// 	console.log("we want to skip the song");
			// 	this.sendNotification("SPOTIFY_NEXT");
			// tell mirror runtime that our data has changed,
			// we will be called back at GetDom() to provide the updated content
			this.updateDom(1000)
		}

	},

	// system notification your module is being hidden
	// typically you would stop doing UI updates (getDom/updateDom) if the module is hidden
	suspend: function(){

	},

	// system notification your module is being unhidden/shown
	// typically you would resume doing UI updates (getDom/updateDom) if the module is shown
	resume: function(){

	},

	// this is the major worker of the module, it provides the displayable content for this module
	getDom: function() {
		var wrapper = document.createElement("div");

		// if user supplied message text in its module config, use it
		if(this.config.hasOwnProperty("message")){
			// using text from module config block in config.js
			wrapper.innerHTML = this.config.message;
			wrapper.className += "PythonPrint"
		}

		// pass the created content back to MM to add to DOM.
		return wrapper;
	},

})
