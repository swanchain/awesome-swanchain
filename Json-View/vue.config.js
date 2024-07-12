'use strict'
const path = require('path')
const webpack = require('webpack')
const UglifyJsPlugin = require('uglifyjs-webpack-plugin');
const CompressionWebpackPlugin = require('compression-webpack-plugin') // gzip压缩
const productionGzipExtensions = /\.(js|css|json|txt|html|ico|svg)(\?.*)?$/i // gzip匹配文件规则
// const BranchVersionWebpackPlugin = require('./webpack-plugin/branch-version-webpack-plugin');
const NOT_DEV = process.env.NODE_ENV !== 'development'

const globalConfig = require('./src/config/index.js')

const resolve = dir => path.join(__dirname, dir)
const addOptions = {
  preserveWhitespace: true
}

module.exports = {
  publicPath: '',

  // 根据环境去打包
  outputDir: process.env.VUE_APP_OUTPUTDIR,

  //是否使用包含运行时编译器的 Vue 构建版本
  runtimeCompiler: true,

  //不在production环境使用SourceMap
  productionSourceMap: false,

  css: {
    loaderOptions: {
      less: {
        javascriptEnabled: true,
      }
    }
  },

  configureWebpack: (config) => {
    config.name = globalConfig.baseTitle //用于设置public/index.html的默认title
    config.entry.app = ['babel-polyfill', './src/main.js']; //入口文件
    let plugins = [
      new UglifyJsPlugin({
        uglifyOptions: {
          warnings: false,
          compress: {
            // drop_console:true,
            drop_debugger: true
          },
          output: {
            // 去掉注释内容
            comments: false,
          }
        },
        sourceMap: false,
        parallel: true,
      }), //删除console插件
      new CompressionWebpackPlugin({
        filename: '[path].gz[query]',
        algorithm: 'gzip',
        test: productionGzipExtensions,
        threshold: 10240, // 只处理比这个值大的资源，按字节计算
        minRatio: 0.8, // 只有压缩率比这个值小的资源才会被处理
        deleteOriginalAssets: false //是否删除原始资源 默认false
      })
    ];
    //只有打包生产环境才需要将console删除
    if (NOT_DEV) {
      config.mode = 'production';
      config.plugins = [...config.plugins, ...plugins];
      config.performance = {
        maxEntrypointSize: 10000000,
        maxAssetSize: 30000000
      }
      // config.plugins.push(new BranchVersionWebpackPlugin());
    }
  },

  //允许对内部的 webpack 配置进行更细粒度的修改。
  chainWebpack: (config) => {
    //命名 
    config.resolve.alias
      .set('@', resolve('src'))
      .set('@api', resolve('src/api'))
      .set('@assets', resolve('src/assets'))
      .set('@components', resolve('src/components'))
      .set('@router', resolve('src/router'))
      .set('@store', resolve('src/store'))
      .set('@utils', resolve('src/utils'))
      .set('@views', resolve('src/views'))
      .set('vue-i18n', 'vue-i18n/dist/vue-i18n.cjs.js')
      .set('@public', resolve('public'));
    //打包文件带hash
    config.output.filename('[name].[hash].js').end();

    //为了补删除换行而加的配置
    config.module
      .rule("vue")
      .use("vue-loader")
      .loader("vue-loader")
      .tap(options => {
        // modify the options...
        options.compilerOptions = addOptions;
        return options;
      });
  },

  devServer: {
    port: 8080,
    open: true, //配置自动启动浏览器
    // proxy: { 
    //   '/api': {
    //     target: 'http://18.221.71.211:5000/',
    //     ws: true,
    //     changeOrigin: true,
    //     secure: false,
    //     pathRewrite: {
    //       '^/api': ''
    //     }
    //   },
    // }
  },

  pluginOptions: {
    i18n: {
      locale: 'en',
      fallbackLocale: 'zn',
      localeDir: 'locales',
      enableLegacy: true,
      runtimeOnly: false,
      compositionOnly: true,
      fullInstall: true
    }
  }
}