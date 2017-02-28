var path = require('path');

module.exports = {
	entry: {
		app: "./js/main.ts"
	},
	output: {
		filename: "[name].js",
		path: path.join(__dirname, "dist")
	},
	module: {
		rules: [
			{test: /\.html$/, loader: "html-loader"},
			{test: /\.(t|j)sx?$/, loader: "ts-loader", exclude: /node_modules/}
		]
	},
	resolve: {
		extensions: ['.ts', '.js']
	}
};
