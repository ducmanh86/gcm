@request.restful()
def index():
    response.view = 'generic.json'
    def GET(*args, **vars):
        # import urllib3
        # pool = urllib3.HTTPSConnectionPool(GCM_SEND_HOST)
        # try:
            # authorization = "key=" + GOOGLE_API_KEY
            # fields = {"data": "manh vo dich", "registration_ids": "APA91bGb976UkwzcEl94k28gICiUjBtEU1SwyaogwhG0HzmEgjdwBGOR6xdExeH0KquIkzWdUwFhJsgtOdypLvptjmwLrV71FN27_Zb8eMUiV1JZH2P5i8SJybxu6jglXRsQVkGnkoTB0GvdEY5Uwka2rO-ZCdYE6EGqTvyR7Wo-6yThP3Klyqs"}
            # headers = {"Authorization": authorization}#, "Content-type": "application/json"}
            # fetch_data = pool.request_encode_body(method = "POST", url = GCM_SEND_URL, fields = fields, headers = headers)
            # print fetch_data.status
            # return str(fetch_data.data)
        # except Exception as ex:
            # return dict(status=400, data=str(ex))

        import urllib
        import urllib2
        try:
            import json
        except ImportError:
            import simplejson as json

        url = 'https://android.googleapis.com/gcm/send'
        values = {"data": {"message": "manh vo dich", "content": "Doi ta co don"}, "registration_ids": ["APA91bGb976UkwzcEl94k28gICiUjBtEU1SwyaogwhG0HzmEgjdwBGOR6xdExeH0KquIkzWdUwFhJsgtOdypLvptjmwLrV71FN27_Zb8eMUiV1JZH2P5i8SJybxu6jglXRsQVkGnkoTB0GvdEY5Uwka2rO-ZCdYE6EGqTvyR7Wo-6yThP3Klyqs"]}
        headers = {'Authorization': 'key=' + GOOGLE_API_KEY,'Content-Type': 'application/json'}
                   
        try:
            # data = urllib.urlencode(values)
            data = json.dumps(values)
            req = urllib2.Request(url, data, headers)
            response = urllib2.urlopen(req)
            the_page = response.read()
            return the_page
        except Exception as ex:
            return dict(status=400, data=str(ex))
        
        return "GET SERVICE"
    def POST(*args, **vars):
        if len(args) != 1:
            return "Parameters invalid!"
        if args[0] == 'register' and 'name' in vars and 'email' in vars and 'regid' in vars:
            name = vars["name"]
            email = vars["email"]
            regid = vars["regid"]
            result = db.gcm_user.insert(name = name, email = email, gcm_id = regid)
            print str(result)
            return str(result)
        elif args[0] == 'send' and 'message' in vars and 'message' in vars:
            regid = vars["regid"]
            message = vars["message"]
            result = db.gcm_user.insert(name = name, email = email, gcm_id = regid)
            return str(result)
        else:
            return "Parameters invalid!"
    def PUT(*args, **vars):
        return "PUT SERVICE"
    def DELETE(*args, **vars):
        return "DELETE SERVICE"
    return locals()
    
# /**
 # * Sending Push Notification
 # */
# public function send_notification($registatoin_ids, $message) {
    # // include config
    # include_once './config.php';

    # // Set POST variables
    # $url = 'https://android.googleapis.com/gcm/send';

    # $fields = array(
        # 'registration_ids' => $registatoin_ids,
        # 'data' => $message,
    # );

    # $headers = array(
        # 'Authorization: key=' . GOOGLE_API_KEY,
        # 'Content-Type: application/json'
    # );
    # // Open connection
    # $ch = curl_init();

    # // Set the url, number of POST vars, POST data
    # curl_setopt($ch, CURLOPT_URL, $url);

    # curl_setopt($ch, CURLOPT_POST, true);
    # curl_setopt($ch, CURLOPT_HTTPHEADER, $headers);
    # curl_setopt($ch, CURLOPT_RETURNTRANSFER, true);

    # // Disabling SSL Certificate support temporarly
    # curl_setopt($ch, CURLOPT_SSL_VERIFYPEER, false);

    # curl_setopt($ch, CURLOPT_POSTFIELDS, json_encode($fields));

    # // Execute post
    # $result = curl_exec($ch);
    # if ($result === FALSE) {
        # die('Curl failed: ' . curl_error($ch));
    # }

    # // Close connection
    # curl_close($ch);
    # echo $result;
# }