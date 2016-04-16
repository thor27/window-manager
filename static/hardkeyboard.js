function HardKeyboard(options) {
    'use strict';
    return this.init(options);
}

(function (window, document) {
  'use strict';

  HardKeyboard.prototype = {

    /**
    Initalizes the form object
    @method init
    **/
    init: function init(options) {
      this.recInterval = null;
      this.connect();

      this.options = options;
      if (options.valid_keys) {
        this.VALID_KEYS = options.valid_keys;
      } else {
        this.VALID_KEYS = [
          'KEY_0','KEY_1', 'KEY_1', 'KEY_2', 'KEY_3', 'KEY_4', 'KEY_5', 'KEY_6',  'KEY_7',  'KEY_8',  'KEY_9',
          'KEY_KP0','KEY_KP1', 'KEY_KP1', 'KEY_KP2', 'KEY_KP3', 'KEY_KP4', 'KEY_KP5', 'KEY_KP6',  'KEY_KP7',  'KEY_KP8',  'KEY_KP9',
        ]
      }
    },
    connect: function connect() {
      var self = this;

      this.socket = new SockJS('http://' + document.domain + ':' + location.port + '/broadcast');

      this.socket.onmessage = function(msg) {
        self.processEvent(JSON.parse(msg.data));
      }

      this.socket.onopen = function () {
          clearInterval(self.recInterval);
      };

      this.socket.onclose = function () {
          self.recInterval = window.setInterval(function () {
            self.connect();
          }, 2000);
      };

    },
    processEvent: function processEvent(msg) {
      if (this.options.textbox) {
        this.simulateKeyboard(this.options.textbox, msg);
      }
    },

    simulateKeyboard: function(box, msg) {
        var element = $(box),
            new_text = '';

        if (msg.type == 'DOWN' || msg.type == 'HOLD') {

          if (msg.keycode == 'KEY_BACKSPACE') {
            new_text = element.text().slice(0,-1)
            element.text(new_text);
          }

          if (this.VALID_KEYS.indexOf(msg.keycode) != -1) {
            var char = msg.keycode.slice(-1);
            element.append(char);
          }

        }
    }
  };

}(window, document));
