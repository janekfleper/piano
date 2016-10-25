html = """<!DOCTYPE html>
<html>
    <head> <title>ESP8266 Piano</title> </head>
    <style>
        .key {padding:100px 20px;}
    </style>
    <body>
        <form id="form_keys" action="/send_key" method="get">
            <input type="hidden" id='freq' name="freq" value="" />
            <button class="key" id="key_c" onmousedown="key_down('c')"
                                onmouseup="key_up()">c</button>
            <button class="key" id="key_d" onmousedown="key_down('d')"
                                onmouseup="key_up()">d</button>
            <button class="key" id="key_e" onmousedown="key_down('e')"
                                onmouseup="key_up()">e</button>
            <button class="key" id="key_f" onmousedown="key_down('f')"
                                onmouseup="key_up()">f</button>
            <button class="key" id="key_g" onmousedown="key_down('g')"
                                onmouseup="key_up()">g</button>
            <button class="key" id="key_a" onmousedown="key_down('a')"
                                onmouseup="key_up()">a</button>
            <button class="key" id="key_b" onmousedown="key_down('b')"
                                onmouseup="key_up()">b</button>
            <button class="key" id="key_C" onmousedown="key_down('C')"
                                onmouseup="key_up()">C</button> <br> <br>
            <button id="led" onclick="toggle_led()">Led</button>
        </form>
    </body>
    <script>
        function key_down(key) {
            document.getElementById("freq").value = key;
            document.getElementById("form_keys").submit();
        }
        function key_up() {
            document.getElementById("freq").value = '0';
            document.getElementById("form_keys").submit();
        }
        function toggle_led() {
            document.getElementById("freq").value = 'led';
            document.getElementById("form_keys").submit();
        }
    </script>
</html>
"""

def get_html():
    return html
