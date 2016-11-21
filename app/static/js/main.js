function webSocket() {
        if("WebSocket" in window || "MozWebSocket" in window){
            var urlPreffix = window.location.protocol != "https:" ? "ws" : "wss",
                $blocker = $("#blocker"),
                $counter = $(".counter", $blocker);

            $blocker.removeClass("hidden");
            $("span", $blocker).addClass("hidden");
            $counter.removeClass("hidden").text("0%");

            var ws4redis = WS4Redis({
                // TODO: replace 'test' with necessary value
                uri: urlPreffix + '://' + document.domain + (location.port ? ":" + location.port : "") + '/ws/' + 'test' + '?subscribe-user',
                receive_message: receiveMessage
            });

            // receive a message though the websocket from the server
            function receiveMessage(msg) {
                $counter.text(parseFloat(JSON.parse(msg).status).toFixed(2) + "%");
                if (JSON.parse(msg).status == 100) {
                    $blocker.addClass("hidden");
                    $("span", $blocker).removeClass("hidden");
                    $counter.addClass("hidden");
                }

            }
        }
}

webSocket();