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
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.0
  scored_at: '2026-08-19'
api_count: 3
apis:
- description: mitmproxy is a free and open source interactive HTTPS proxy for intercepting, inspecting, modifying, and replaying HTTP and HTTPS traffic. It provides console-based, web-based, and command-line interf
  name: Mitmproxy
  slug: mitmproxy
- description: mitmweb is the web-based interface for mitmproxy, providing a graphical user interface in the browser for intercepting and inspecting HTTP and HTTPS traffic flows.
  name: Mitmweb
  slug: mitmweb
- description: mitmdump is the command-line companion to mitmproxy, providing tcpdump-like functionality for HTTP and HTTPS traffic. It can be used for scripted traffic manipulation and automated testing workflows.
  name: Mitmdump
  slug: mitmdump
artifact_total: 7
common:
- group: auth
  title: ''
  type: DomainSecurity
  url: security/mitmproxy-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/mitmproxy
- group: company
  title: ''
  type: Website
  url: https://mitmproxy.org
- group: docs
  title: ''
  type: Documentation
  url: https://docs.mitmproxy.org/stable/
- group: build
  title: ''
  type: GitHub
  url: https://github.com/mitmproxy/mitmproxy
- group: company
  title: ''
  type: Blog
  url: https://mitmproxy.org/posts/
- group: operate
  title: ''
  type: ReleaseNotes
  url: https://github.com/mitmproxy/mitmproxy/releases
- group: operate
  title: ''
  type: Issues
  url: https://github.com/mitmproxy/mitmproxy/issues
- group: commercial
  title: ''
  type: License
  url: https://github.com/mitmproxy/mitmproxy/blob/main/LICENSE
- group: other
  title: ''
  type: PyPI
  url: https://pypi.org/project/mitmproxy/
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/maboroshi_inc
created: '2026-03-26'
description: mitmproxy is a free and open source interactive HTTPS proxy that allows developers and security researchers to intercept, inspect, modify, and replay HTTP and HTTPS traffic flows. It includes mitmproxy (interactive console), mitmweb (web-based interface), and mitmdump (command-line tool), providing powerful capabilities for debugging, testing, and analyzing API traffic and web applications.
finops:
- name: Mitmproxy Finops
  service_category: API
  slug: mitmproxy-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/mitmproxy.png
layout: provider
modified: '2026-04-28'
name: Mitmproxy
nav: Providers
network: true
overview: 'Mitmproxy publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Testing, HTTP Debugging, HTTPS Proxy, Open Source, and Security Testing.


  Mitmproxy''s developer surface includes documentation, GitHub presence, engineering blog, release notes, and 7 more developer resources.'
plans:
- name: Mitmproxy Plans Pricing
  plan_count: 3
  slug: mitmproxy-plans-pricing
random_paper: 123
rate_limits:
- limit_count: 5
  name: Mitmproxy Rate Limits
  slug: mitmproxy-rate-limits
score:
  band: emerging
  composite: 15.4
  delta: -0.2
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 26.3
  previous_composite: 15.6
  schema_version: 0.12.0
  scored_at: '2026-08-19'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/mitmproxy/refs/heads/main/screenshots/mitmproxy-2026-06-20T185616.png
security:
- kind: domain-security
  name: Mitmproxy Domain Security
  slug: mitmproxy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: mitmproxy
tags:
- API Testing
- HTTP Debugging
- HTTPS Proxy
- Open Source
- Security Testing
- Traffic Analysis
- Traffic Interception
website: https://mitmproxy.org
---
