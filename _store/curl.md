---
aid: curl
name: cURL
description: cURL is a command-line tool and library for transferring data with URLs. Originally released in 1997 by Daniel Stenberg, cURL is the de facto standard tool used by developers for testing, automating, and scripting interactions with HTTP, HTTPS, FTP, and many other URL-based protocols. It ships in two primary forms - the curl command-line binary used directly in shells and scripts, and libcurl, a portable C library that powers data transfer features inside thousands of applications, operating systems, devices, and programming languages.
url: https://raw.githubusercontent.com/api-evangelist/curl/refs/heads/main/apis.yml
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - API Client
  - Command Line
  - Data Transfer
  - FTP
  - HTTP
  - HTTPS
  - Library
  - Network Tools
  - Open Source
  - REST
created: '2024-01-01'
modified: '2026-04-28'
specificationVersion: '0.20'
apis:
  - aid: curl:curl-cli
    name: cURL Command Line Tool
    description: The curl command-line tool transfers data to or from a server using URL syntax, supporting protocols including DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, RTMP, RTSP, SCP, SFTP, SMB, SMTP, SMTPS, TELNET, TFTP, WS and WSS. It is widely used for API testing, automation, scripting, file uploads and downloads, debugging HTTP exchanges, and as a general-purpose network client.
    image: https://curl.se/logo/curl-logo.svg
    humanURL: https://curl.se/
    tags:
      - API Client
      - API Testing
      - Command Line
      - Data Transfer
      - FTP
      - HTTP
      - HTTPS
      - REST
    properties:
      - type: Documentation
        url: https://curl.se/docs/
      - type: Manual
        url: https://curl.se/docs/manual.html
      - type: Tutorial
        url: https://curl.se/docs/tutorial.html
      - type: Man Page
        url: https://curl.se/docs/manpage.html
      - type: How To
        url: https://curl.se/docs/howto.html
      - type: FAQ
        url: https://curl.se/docs/faq.html
      - type: GitHub
        url: https://github.com/curl/curl
      - type: Download
        url: https://curl.se/download.html
      - type: Changelog
        url: https://curl.se/changes.html
  - aid: curl:libcurl
    name: libcurl
    description: libcurl is a free, easy-to-use, thread-safe, IPv6-compatible client-side URL transfer library written in C with a stable API and ABI. It supports the same broad set of protocols as the curl command-line tool and is embedded in operating systems, applications, and developer tools across nearly every platform. Bindings are available for dozens of languages including PHP, Python, Ruby, Rust, Go, Java, .NET, and many others.
    image: https://curl.se/logo/curl-logo.svg
    humanURL: https://curl.se/libcurl/
    tags:
      - C
      - HTTP Client
      - Library
      - SDK
      - URL Transfer
    properties:
      - type: Documentation
        url: https://curl.se/libcurl/
      - type: API Reference
        url: https://curl.se/libcurl/c/
      - type: Examples
        url: https://curl.se/libcurl/c/example.html
      - type: Bindings
        url: https://curl.se/libcurl/bindings.html
      - type: GitHub
        url: https://github.com/curl/curl
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
common:
  - type: Website
    url: https://curl.se/
  - type: Support
    url: https://curl.se/support.html
  - type: Mailing Lists
    url: https://curl.se/mail/
  - type: Security
    url: https://curl.se/dev/security.html
  - type: Blog
    url: https://daniel.haxx.se/blog/
  - type: Books
    url: https://everything.curl.dev/
  - type: License
    url: https://curl.se/docs/copyright.html
---
