const path = require('path');
const SRC_DIR = path.join(__dirname, 'client', 'src');
const DIST_DIR = path.join(__dirname, 'client', 'static');
const BundleTracker = require("webpack-bundle-tracker");

module.exports = {
  mode: 'development',
  target: 'web',
  entry: {
    app: `${SRC_DIR}/index.jsx`
  },
  output: {
    path: DIST_DIR,
    filename: 'bundle.js'
  },
  module: {
    rules: [
      {
        test: /\.css$/i,
        use: ['style-loader',
          {
            loader: 'css-loader',
            options: {
              importLoaders: 1,
              modules: true
            }
          }
        ]
      },
      {
        test: [/\.jsx$/],
        exclude: /node_modules/,
        use: {
          loader: 'babel-loader',
          options: {
            presets: ['@babel/preset-env', '@babel/preset-react'],
            plugins: ['@babel/plugin-transform-runtime', '@babel/plugin-proposal-class-properties']
          }
        },
      }
    ],
  },
  optimization: { minimize: true },
  plugins: [
    new BundleTracker({
      path: __dirname,
      publicPath: '/static/',
      filename: 'webpack-stats.dev.json'
    })
  ]
}