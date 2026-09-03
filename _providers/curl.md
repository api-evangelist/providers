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
agent_readiness:
  band: human-only
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: documented
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.8
  scored_at: '2026-09-03'
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
overview: 'cURL publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Client, Command Line, Data Transfer, FTP, and HTTP.


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
score:
  band: emerging
  composite: 21.3
  coverage:
    artifact_dirs: 6
    catalog_gap: 74.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 6.7
    developer_ergonomics: 31.0
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 39.5
  previous_composite: 21.3
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 22.2
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
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
- FTP
- HTTP
- HTTPS
- Library
- Network Tools
- Open-Source
- REST
website: https://curl.se/
---
