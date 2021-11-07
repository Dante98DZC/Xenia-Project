
(function ($) {
  'use strict';

  const FULL_DASH_ARRAY = 283;
  const WARNING_THRESHOLD = 0.50;
  const ALERT_THRESHOLD = 0.20;
  const COLOR_CODES = {
    info: {
      color: "green"
    },
    warning: {
      color: "orange",
      threshold: WARNING_THRESHOLD
    },
    alert: {
      color: "red",
      threshold: ALERT_THRESHOLD
    }
  };
  $.fn.timer = function (options) {

    var settings = $.extend({
      duration: 60,
      current: 0,
    }, options);

    const TIME_LIMIT = settings.duration * 60;
    let timePassed = settings.current * 60;
    let timeLeft = TIME_LIMIT - timePassed;
    let timerInterval = null;
    let remainingPathColor = COLOR_CODES.info.color;
    return this.each(function () {
      var $$ = $(this);

      $$.html(`
      <div class="base-timer">
        <svg class="base-timer__svg" viewBox="0 0 100 100" xmlns="http://www.w3.org/2000/svg">
          <g class="base-timer__circle">
            <circle class="base-timer__path-elapsed" cx="50" cy="50" r="45"></circle>
            <path
              id="base-timer-path-remaining"
              stroke-dasharray="283"
              class="base-timer__path-remaining ${remainingPathColor}"
              d="
                M 50, 50
                m -45, 0
                a 45,45 0 1,0 90,0
                a 45,45 0 1,0 -90,0
              "
            ></path>
          </g>
        </svg>
        <span id="base-timer-label" class="base-timer__label">${formatTime(
          timeLeft
        )}</span>
      </div>
      `);
      var path = $("#base-timer-path-remaining",$$)
      var base_label = $("#base-timer-label",$$)
    startTimer();

    function onTimesUp() {
      clearInterval(timerInterval);
    }
    
    function startTimer() {
      timerInterval = setInterval(() => {
        timePassed = timePassed += 1;
        timeLeft = TIME_LIMIT - timePassed;
        base_label.innerHTML = formatTime(
          timeLeft
        );
        setCircleDasharray();
        setRemainingPathColor(timeLeft);
    
        if (timeLeft === 0) {
          onTimesUp();
        }
      }, 1000);
    }
    
    function formatTime(time) {
      return `${Math.floor(time / 60)}`;
    }
    
    function setRemainingPathColor(timeLeft) {
      const { alert, warning, info } = COLOR_CODES;
      if (timeLeft/TIME_LIMIT <= alert.threshold) {
        path.removeClass(warning.color);
        path.addClass(alert.color);
      } else if (timeLeft/TIME_LIMIT <= warning.threshold) {
        path.removeClass(info.color);
        path.addClass(warning.color);
      }
    }
    
    function calculateTimeFraction() {
      const rawTimeFraction = timeLeft / TIME_LIMIT;
      return rawTimeFraction - (1 / TIME_LIMIT) * (1 - rawTimeFraction);
    }
    
    function setCircleDasharray() {
      const circleDasharray = `${(
        calculateTimeFraction() * FULL_DASH_ARRAY
      ).toFixed(0)} 283`;
      path.attr("stroke-dasharray", circleDasharray);
    } 
    });
  };
}(jQuery));