const path = require('path');
const SRC_DIR = path.join(__dirname, 'client', 'src');
const DIST_DIR = path.join(__dirname, 'client', 'static');
const HtmlWebpackPlugin = require('html-webpack-plugin');
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  mode: 'development',
  target: 'web',
  entry: {
    app: `${SRC_DIR}/index.jsx`
  },
  output: {
    path: DIST_DIR,
    publicPath: 'http://0.0.0.0:8000/static/',
    filename: 'bundle.js'
  },
  module: {
    rules: [{
      test: [/\.jsx$/],
      exclude: /node_modules/,
      use: {
        loader: 'babel-loader',
        options: {
          presets: ['@babel/preset-react', '@babel/preset-env']
        }
      },
    }],
  },
  plugins: [
    new HtmlWebpackPlugin({
      title: 'Crypto',
      template: path.join(__dirname, 'client', 'templates', 'index.html'),
      filename: 'index.html'
    }),
    new BundleTracker({
      path: __dirname,
      filename: 'webpack-stats.dev.json'
    })
  ]
}