---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - plans
  trial: false
  try_now: false
api_count: 2
apis:
- description: 'The curl command-line tool transfers data to or from a server using URL syntax, supporting protocols including DICT, FILE, FTP, FTPS, GOPHER, HTTP, HTTPS, IMAP, IMAPS, LDAP, LDAPS, MQTT, POP3, POP3S, '
  name: cURL Command Line Tool
  slug: curl-cli
- description: libcurl is a free, easy-to-use, thread-safe, IPv6-compatible client-side URL transfer library written in C with a stable API and ABI. It supports the same broad set of protocols as the curl command-li
  name: libcurl
  slug: libcurl
artifact_total: 7
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/curl-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/curl-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-curl-project
- group: company
  title: ''
  type: Website
  url: https://curl.se/
- group: operate
  title: ''
  type: Support
  url: https://curl.se/support.html
- group: other
  title: ''
  type: Mailing Lists
  url: https://curl.se/mail/
- group: auth
  title: ''
  type: Security
  url: https://curl.se/dev/security.html
- group: company
  title: ''
  type: Blog
  url: https://daniel.haxx.se/blog/
- group: other
  title: ''
  type: Books
  url: https://everything.curl.dev/
- group: commercial
  title: ''
  type: License
  url: https://curl.se/docs/copyright.html
created: '2024-01-01'
description: cURL is a command-line tool and library for transferring data with URLs. Originally released in 1997 by Daniel Stenberg, cURL is the de facto standard tool used by developers for testing, automating, and scripting interactions with HTTP, HTTPS, FTP, and many other URL-based protocols. It ships in two primary forms - the curl command-line binary used directly in shells and scripts, and libcurl, a portable C library that powers data transfer features inside thousands of applications, operating systems, devices, and programming languages.
finops:
- name: Curl Finops
  service_category: API
  slug: curl-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/curl.png
layout: provider
modified: '2026-04-28'
name: cURL
nav: Providers
network: true
overview: 'cURL publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Client, Command Line, Data Transfer, Developer Tools, and FTP.


  cURL''s developer surface includes support, engineering blog, and 8 more developer resources.'
plans:
- name: Curl Plans Pricing
  plan_count: 3
  slug: curl-plans-pricing
random_paper: 18
rate_limits:
- limit_count: 5
  name: Curl Rate Limits
  slug: curl-rate-limits
screenshot: https://raw.githubusercontent.com/api-evangelist/curl/refs/heads/main/screenshots/curl-2026-06-20T175333.png
security:
- kind: domain-security
  name: Curl Domain Security
  slug: curl-domain-security
  summary_line: TLSv1.3 · HSTS
- kind: vulnerability-disclosure
  name: Curl Vulnerability Disclosure
  slug: curl-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: curl
tags:
- API Client
- Command Line
- Data Transfer
- Developer Tools
- FTP
- HTTP
- HTTPS
- Library
- Network Tools
- Open-Source
- REST
website: https://curl.se/
---
