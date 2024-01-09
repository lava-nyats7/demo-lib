from elasticsearch import Elasticsearch, ConnectionError, ConnectionTimeout, SSLError

class ElasticsearchConnection:
    def __init__(self, host, port, username=None, password=None, use_https=False, timeout=30):
        self.host = host
        self.port = port
        self.username = username
        self.password = password
        self.use_https = use_https
        self.timeout = timeout
        self.connection = None

        self._establish_connection()

    def _construct_url(self):
        def _construct_url(self):
            url = f"http://{self.host}:{self.port}"
            if self.use_https:
                url = f"https://{self.host}:{self.port}"
            return url

    def _establish_connection(self):
        try:
            url = self._construct_url()
            if self.username and self.password:
                self.connection = Elasticsearch(
                    [url],
                    http_auth=(self.username, self.password),
                    verify_certs=False,  # Disable SSL verification (use True in production)
                    timeout=self.timeout
                )
            else:
                self.connection = Elasticsearch(
                    [url],
                    verify_certs=False,  # Disable SSL verification (use True in production)
                    timeout=self.timeout
                )
        except ConnectionError as ce:
            raise ConnectionError(f"ConnectionError: {ce}")
        except ConnectionTimeout as cte:
            raise ConnectionTimeout(f"ConnectionTimeout: {cte}")
        except SSLError as ssle:
            raise SSLError(f"SSLError: {ssle}")

    def get_connection(self):
        if self.connection:
            return self.connection
        else:
            raise ConnectionError("Elasticsearch connection is not established.")

# Example usage:
# try:
    #es_connection = ElasticsearchConnection(host='13.233.85.187', port=9200, username='elastic', password='AVEKSHAA2023APPNEURA', use_https=True)
    #es = es_connection.get_connection()
#
#     # Now 'es' is your Elasticsearch connection object, and you can use it in your project.
#     # For example:
#     #res = es.search(index="tcl_dynatrace_alert_2024_week_1", body={"query": {"match_all": {}}})
#     #print(res)
# except ConnectionError as ce:
#     print(f"Failed to establish Elasticsearch connection: {ce}")
# except Exception as e:
#     print(f"An unexpected error occurred: {e}")
