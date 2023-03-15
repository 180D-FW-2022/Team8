var NodeHelper = require("node_helper");
//const { PythonShell } = require("python-shell");
const { spawn } = require('child_process');
const path = require('path')


module.exports = NodeHelper.create({
	launchit(){
		let handler
		if(this.config.debug) console.log("VoiceControl spawning "+this.config.command+" using "+this.config.pythonName)
		handler = spawn(this.config.pythonName, ['-u', this.config.command]);
		handler.stdout.on('data', (data) => {
			if(this.config.debug) console.log("VoiceControl sending program output="+data)
			this.sendSocketNotification("WAKE_DETECTED", data.toString())
		})
		handler.stderr.on('data', (data)=>{
			if(this.config.debug) console.log("VoiceControl program error="+data)
		})
		handler.on('error', (error)=>{
			if(this.config.debug) console.log("VoiceControl spawn error="+data)
		})
		//launch_script += 1;
	},
	startit(){

		if(this.config.command.startsWith(this.config.pythonName))
			this.config.command=this.config.command.slice(this.config.pythonName.length)
		if(this.config.localfolder)
			this.config.command=__dirname+path.sep+this.config.command
		if(this.config.repetative)
			this.launchit()
		else
			 setInterval( ()=>{ this.launchit() }, this.config.cycletime )
		},

	// handle messages from our module// each notification indicates a different messages
	// payload is a data structure that is different per message.. up to you to design this
	socketNotificationReceived(notification, payload) {
		console.log(this.name + " received a socket notification: " + notification + " - Payload: " + payload);
		// if config message from module
		if (notification === "CONFIG") {
			// save payload config info
			this.config=payload
			// wait 15 seconds, send a message back to module
			this.startit()
		}

	},

});