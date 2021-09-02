**golden-config | python - NSO by API´s**.




**Use Case Description**. 

For this particular use case, referring to the configuration of network services, when finishing adding the configuration of the equipment that is being managed in the web portal, this data must be sent to the orchestrator's methods so that it fulfills its function. , the data sent by the web part to the orchestrator, are necessary to carry out its activities until the team is enabled.

**Installation**.

Detailed instructions on how to install, configure, and get the project running. Call out any dependencies. This should be frequently tested and updated to make sure it works reliably, accounts for updated versions of dependencies, etc.

Configuration
If the code is configurable, describe it in detail, either here or in other documentation that you reference.

Usage
Show users how to use the code. Be specific. Use appropriate formatting when showing code snippets or command line output.

DevNet Sandbox
A great way to make your repo easy for others to use is to provide a link to a DevNet Sandbox that provides a network or other resources required to use this code. In addition to identifying an appropriate sandbox, be sure to provide instructions and any configuration necessary to run your code with the sandbox.

How to test the software
Provide details on steps to test, versions of components/dependencies against which code was tested, date the code was last tested, etc. If the repo includes automated tests, detail how to run those tests. If the repo is instrumented with a continuous testing framework, that is even better.

Known issues
Document any significant shortcomings with the code. If using GitHub Issues to track issues, make that known and provide any templates or conventions to be followed when opening a new issue.

Getting help
Instruct users how to get help with this code; this might include links to an issues list, wiki, mailing list, etc.

Example

If you have questions, concerns, bug reports, etc., please create an issue against this repository.

Getting involved
This section should detail why people should get involved and describe key areas you are currently focusing on; e.g., trying to get feedback on features, fixing certain bugs, building important pieces, etc. Include information on how to setup a development environment if different from general installation instructions.

General instructions on how to contribute should be stated with a link to CONTRIBUTING file.

Credits and references
Projects that inspired you
Related projects
Books, papers, talks, or other sources that have meaningful impact or influence on this code
Licensing info
A license is required for others to be able to use your code. An open source license is more than just a usage license, it is license to contribute and collaborate on code. Open sourcing code and contributing it to Code Exchange or Automation Exchange requires a commitment to maintain the code and help the community use and contribute to the code.

Choosing a license can be difficult and depend on your goals for your code, other licensed code on which your code depends, your business objectives, etc. This template does not intend to provide legal advise. You should seek legal counsel for that. However, in general, less restrictive licenses make your code easier for others to use.

Cisco employees can find licensing options and guidance here.

Once you have determined which license is appropriate, GitHub provides functionality that makes it easy to add a LICENSE file to a GitHub repo, either when creating a new repo or by adding to an existing repo.

When creating a repo through the GitHub UI, you can click on Add a license and select from a set of OSI approved open source licenses. See detailed instructions.

Once a repo has been created, you can easily add a LICENSE file through the GitHub UI at any time. Simply select Create New File, type LICENSE into the filename box, and you will be given the option to select from a set of common open source licenses. See detailed instructions.

Once you have created the LICENSE file, be sure to update/replace any templated fields with appropriate information, including the Copyright. For example, the 3-Clause BSD license template has the following copyright notice:

Copyright (c) <YEAR>, <COPYRIGHT HOLDER>

See the LICENSE for this template repo as an example.

Once your LICENSE file exists, you can delete this section of the README, or replace the instructions in this section with a statement of which license you selected and a link to your license file, e.g.

This code is licensed under the BSD 3-Clause License. See LICENSE for details.

Some licenses, such as Apache 2.0 and GPL v3, do not include a copyright notice in the LICENSE itself. In such cases, a NOTICE file is a common place to include a copyright notice. For a very simple example, see NOTICE.

In the event you make use of 3rd party code, it is required by some licenses, and a good practice in all cases, to provide attribution for all such 3rd party code in your NOTICE file. For a great example, see https://github.com/cisco/ChezScheme/blob/master/NOTICE.

Best practices
Information below can help you make your repo meet our requirements and be more useful to others.

Good practices
Manage sensitive data for scripts. For example, store passwords/API keys and other sensitive data in env.py or parse it as arguments. In Python, you can use ConfigParser for applications and programs: encrypt sensitive data in your database.
Include in Installation section how to run your script for different OS like Windows/macOS/Linux.
Print usage if you run script or program without any input data (support -h -help flags).
Catch an error and print useful information in console and interface.
Add error management to handle if users miss some parameters or add them in the wrong format.
Add links for resources where users can test code/app. For example, add links DevNet sandboxs (Always-on or reservable). You can find a list of all available sandboxes here https://devnetsandbox.cisco.com/RM/Topology.
Add links where users can download and how to install additional soft/app/libraries that are needed to run your code. For example, installer for Python, node, and so on.
Add a NOTICE file with copyright if you use GPLv3 or Apache 2.0 license (sample NOTICE file).
Dockerize app or part of an app like server/client.
At the top of the Readme.md file add a hash symbol and the full use case name to create a useful Readme title. As an example, write # Devicebanner, updates the banner motd on a network device instead of just 'devicebanner'.
If your repo is connected with Cisco SecureX orchestration workflow, please check if your workflow or atomic action conforms to their best practices using this tool.
Bad practices
Use bad quality screenshots.
Users need to rename some files like variables_template.py.
Users need to include credentials in source files.
Don’t describe in which format users need to type or paste in file API endpoint or server IP. For example, sometimes devs write in code api_endpoint = “https://" + IP +"/", such that users need to paste the IP only without a slash at the end or a protocol specification. Please clarify this information in README.
