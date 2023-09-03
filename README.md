

    <h1>URL Status Checker</h1>

    <p>This Python script is designed to extract URLs from an input file that contain GET parameters, check their HTTP status codes, and save the results in output files. It uses the `urllib.parse` library to parse URLs and the `requests` library to make HTTP requests.</p>

    <h2>Features</h2>

    <ul>
        <li>Extract URLs with GET parameters.</li>
        <li>Check HTTP status codes of extracted URLs.</li>
        <li>Save all results in an output file.</li>
        <li>Save URLs with a status code of 200 (OK) in a separate success file.</li>
    </ul>

    <h2>Installation</h2>

    <ol>
        <li>Clone or download this repository to your local machine.</li>
        <li>Open your terminal or command prompt.</li>
        <li>Navigate to the directory where the script is located.</li>
        <li>Install the required Python libraries using the following command:</li>
    </ol>

    <pre><code>pip install urllib3 requests</code></pre>

    <h2>How to Use</h2>

    <ol>
        <li>Run the script in your terminal:</li>
    </ol>

    <pre><code>python url_status_checker.py</code></pre>

    <li>Follow the on-screen prompts:</li>

    <ul>
        <li>Enter the path to the input file containing URLs.</li>
        <li>Specify the path to the output file to save all results.</li>
        <li>Specify the path to the output file to save success URLs (HTTP 200).</li>
    </ul>

    <li>The script will process the URLs, check their status codes, and save the results in the specified output files.</li>

    <h2>Example Usage</h2>

    <pre><code>python url_status_checker.py</code></pre>
    <pre><code>Enter the path to the input file containing URLs: input.txt</code></pre>
    <pre><code>Enter the path to the output file to save all results: all_results.txt</code></pre>
    <pre><code>Enter the path to the output file to save success URLs (HTTP 200): success_urls.txt</code></pre>


