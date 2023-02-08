/* MagicMirror²
 * Module: HelloWorld
 *
 * By Michael Teeuw https://michaelteeuw.nl
 * MIT Licensed.
 */
Module.register("helloworld", {
	// Default module config.
	defaults: {
		text: "Hello World!"
	},

	getTemplate: function () {
		return "helloworld.njk";
	},

	getTemplateData: function () {
		return this.config;
	},

	notificationReceived: function (notification, payload, sender) {
		if (notification === "TESTING"){
		  Log.log(this.name + "has caught the test notification");
		}
	},
});
