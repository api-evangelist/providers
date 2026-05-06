---
aid: mitmproxy
name: Mitmproxy
description: mitmproxy is a free and open source interactive HTTPS proxy that allows developers and security researchers to intercept, inspect, modify, and replay HTTP and HTTPS traffic flows. It includes mitmproxy (interactive console), mitmweb (web-based interface), and mitmdump (command-line tool), providing powerful capabilities for debugging, testing, and analyzing API traffic and web applications.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Testing
  - HTTP Debugging
  - HTTPS Proxy
  - Open Source
  - Security Testing
  - Traffic Analysis
  - Traffic Interception
url: https://raw.githubusercontent.com/api-evangelist/mitmproxy/refs/heads/main/apis.yml
created: '2026-03-26'
modified: '2026-04-28'
specificationVersion: '0.19'
apis:
  - aid: mitmproxy:mitmproxy
    name: Mitmproxy
    description: mitmproxy is a free and open source interactive HTTPS proxy for intercepting, inspecting, modifying, and replaying HTTP and HTTPS traffic. It provides console-based, web-based, and command-line interfaces for working with network traffic flows.
    humanURL: https://mitmproxy.org
    tags:
      - API Testing
      - HTTP Debugging
      - HTTPS Proxy
      - Traffic Analysis
      - Traffic Interception
    properties:
      - type: Documentation
        url: https://docs.mitmproxy.org/stable/
      - type: GettingStarted
        url: https://docs.mitmproxy.org/stable/overview-getting-started/
      - type: GitHubOrganization
        url: https://github.com/mitmproxy/mitmproxy
      - type: Installation
        url: https://docs.mitmproxy.org/stable/overview-installation/
  - aid: mitmproxy:mitmweb
    name: Mitmweb
    description: mitmweb is the web-based interface for mitmproxy, providing a graphical user interface in the browser for intercepting and inspecting HTTP and HTTPS traffic flows.
    humanURL: https://docs.mitmproxy.org/stable/overview-tools/#mitmweb
    tags:
      - HTTPS Proxy
      - Traffic Inspection
      - Web Interface
    properties:
      - type: Documentation
        url: https://docs.mitmproxy.org/stable/overview-tools/#mitmweb
  - aid: mitmproxy:mitmdump
    name: Mitmdump
    description: mitmdump is the command-line companion to mitmproxy, providing tcpdump-like functionality for HTTP and HTTPS traffic. It can be used for scripted traffic manipulation and automated testing workflows.
    humanURL: https://docs.mitmproxy.org/stable/overview-tools/#mitmdump
    tags:
      - Command Line
      - Scripting
      - Traffic Dump
    properties:
      - type: Documentation
        url: https://docs.mitmproxy.org/stable/overview-tools/#mitmdump
common:
  - type: Website
    url: https://mitmproxy.org
  - type: Documentation
    url: https://docs.mitmproxy.org/stable/
  - type: GitHub
    url: https://github.com/mitmproxy/mitmproxy
  - type: Blog
    url: https://mitmproxy.org/posts/
  - type: Releases
    url: https://github.com/mitmproxy/mitmproxy/releases
  - type: Issues
    url: https://github.com/mitmproxy/mitmproxy/issues
  - type: License
    url: https://github.com/mitmproxy/mitmproxy/blob/main/LICENSE
  - type: PyPI
    url: https://pypi.org/project/mitmproxy/
  - type: Twitter
    url: https://twitter.com/maboroshi_inc
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
