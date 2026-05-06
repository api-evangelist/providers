---
aid: wireshark
name: Wireshark
description: Wireshark is the world's foremost and widely-used free and open-source network protocol analyzer. It lets you capture and interactively browse the traffic running on a computer network. Wireshark provides a powerful dissector framework with a Lua scripting API, C/C++ plugin architecture, TShark command-line tools, and the libwireshark library for developers building network analysis tools.
type: Index
url: https://raw.githubusercontent.com/api-evangelist/wireshark/refs/heads/main/apis.yml
tags:
  - Debugging
  - Network Analysis
  - Open Source
  - Packet Capture
  - Protocol Analysis
  - Security
created: '2025-01-08'
modified: '2026-05-03'
specificationVersion: '0.19'
access: 3rd-Party
position: Consumer
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
apis:
  - aid: wireshark:wireshark
    name: Wireshark
    description: Wireshark is a free and open-source network protocol analyzer that captures and interactively browses network traffic. It supports hundreds of protocols, runs on multiple platforms, and provides deep inspection of packets. Developers can extend Wireshark through its Lua scripting API, C/C++ dissector plugins, Extcap plugin interface, and the Wiretap library for custom capture file formats.
    humanURL: https://www.wireshark.org
    tags:
      - Debugging
      - Extcap
      - Lua Scripting
      - Network Analysis
      - Open Source
      - Packet Capture
      - Protocol Analysis
      - Plugins
    properties:
      - type: Documentation
        url: https://www.wireshark.org/docs/
      - type: APIReference
        url: https://www.wireshark.org/docs/wsdg_html_chunked/
      - type: GettingStarted
        url: https://www.wireshark.org/docs/wsug_html_chunked/
      - type: SDK
        url: https://www.wireshark.org/docs/wsdg_html_chunked/ChapterDissection.html
        title: Dissector Plugin API (C/C++)
      - type: SDK
        url: https://www.wireshark.org/docs/wsdg_html_chunked/wsluarm.html
        title: Lua API Reference
      - type: Downloads
        url: https://www.wireshark.org/download.html
common:
  - type: Website
    url: https://www.wireshark.org
  - type: Documentation
    url: https://www.wireshark.org/docs/
  - type: Blog
    url: https://blog.wireshark.org
  - type: FAQ
    url: https://www.wireshark.org/faq.html
  - type: GitHub
    url: https://github.com/wireshark/wireshark
  - type: GitLab
    url: https://gitlab.com/wireshark/wireshark
  - type: Support
    url: https://ask.wireshark.org
  - type: Downloads
    url: https://www.wireshark.org/download.html
  - type: ReleaseNotes
    url: https://www.wireshark.org/docs/relnotes/
  - type: Forum
    url: https://www.wireshark.org/lists/
  - type: Features
    data:
      - name: Packet Capture
        description: Capture live network traffic from multiple interfaces simultaneously using libpcap/Npcap.
      - name: Deep Packet Inspection
        description: Analyze hundreds of protocols with full decode of packet fields and values.
      - name: Display Filters
        description: Powerful filter language for drilling into captured traffic.
      - name: Lua Scripting
        description: Extend Wireshark with custom dissectors, listeners, and menus using the Lua API.
      - name: Dissector Plugins
        description: Write C/C++ plugins to add support for new protocols.
      - name: TShark CLI
        description: Command-line version of Wireshark for scripting and automation.
      - name: Extcap Interface
        description: Plugin API to add custom capture sources to Wireshark.
      - name: Wiretap Library
        description: Library for reading and writing capture file formats including pcap and pcapng.
  - type: UseCases
    data:
      - name: Network Troubleshooting
        description: Diagnose latency, packet loss, and protocol errors in live or captured traffic.
      - name: API Traffic Debugging
        description: Inspect raw HTTP, gRPC, and WebSocket API requests and responses at the packet level.
      - name: Protocol Development
        description: Develop and test new network protocols using Wireshark dissectors.
      - name: Security Analysis
        description: Analyze network traffic for intrusion indicators and malicious patterns.
      - name: Education
        description: Learn networking concepts by capturing and examining real protocol exchanges.
  - type: Integrations
    data:
      - name: TShark
        description: Command-line packet analyzer that uses the same dissection engine as Wireshark.
      - name: dumpcap
        description: Minimal capture utility used by Wireshark and TShark.
      - name: editcap
        description: Utility for editing and converting capture files.
      - name: Lua
        description: Scripting language embedded in Wireshark for custom protocol dissectors.
      - name: libpcap/Npcap
        description: Packet capture libraries used by Wireshark on Unix and Windows respectively.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
