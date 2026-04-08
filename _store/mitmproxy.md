---
aid: mitmproxy
url: https://raw.githubusercontent.com/api-evangelist/mitmproxy/refs/heads/main/apis.yml
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
name: Mitmproxy
tags:
- API Testing
- HTTP Debugging
- HTTPS Proxy
- Open Source
- Security Testing
- Traffic Analysis
- Traffic Interception
type: Contract
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
access: 3rd-Party
created: '2026-03-29'
modified: '2026-04-07'
position: Consuming
description: mitmproxy is a free and open source interactive HTTPS proxy that allows developers and security researchers to intercept, inspect, modify, and replay HTTP and HTTPS traffic flows. It includes mitmproxy (interactive console), mitmweb (web-based interface), and mitmdump (command-line tool), providing powerful capabilities for debugging, testing, and analyzing API traffic and web applications.
maintainers:
- FN: Kin Lane
  email: info@apievangelist.com
specificationVersion: '0.19'
---

