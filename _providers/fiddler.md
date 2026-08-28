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
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 2.5
  scored_at: '2026-08-26'
api_count: 3
apis:
- description: Fiddler Everywhere is a cross-platform web debugging proxy for macOS, Windows, and Linux. It captures HTTP and HTTPS traffic, provides API composition capabilities, and includes collaboration features
  name: Fiddler Everywhere
  slug: fiddler-everywhere
- description: Fiddler Classic is the original free Windows-based HTTP debugging proxy for logging all HTTP and HTTPS traffic between a computer and the Internet. It supports traffic inspection, breakpoints, and ext
  name: Fiddler Classic
  slug: fiddler-classic
- description: Fiddler Jam is a browser-based troubleshooting solution that enables non-technical users to capture HTTP traffic logs and share them with development teams for collaborative debugging of web issues an
  name: Fiddler Jam
  slug: fiddler-jam
artifact_total: 8
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/fiddler-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/fiddler-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/fiddler-labs
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/fiddler-ai
- group: company
  title: ''
  type: Website
  url: https://www.telerik.com/fiddler
- group: docs
  title: ''
  type: Documentation
  url: https://docs.telerik.com/fiddler-everywhere/introduction
- group: company
  title: ''
  type: Blog
  url: https://www.telerik.com/blogs/fiddler
- group: commercial
  title: ''
  type: Pricing
  url: https://www.telerik.com/purchase/fiddler
- group: other
  title: ''
  type: Download
  url: https://www.telerik.com/download/fiddler-everywhere
- group: operate
  title: ''
  type: Support
  url: https://www.telerik.com/support/fiddler-everywhere
- group: start
  title: ''
  type: Login
  url: https://www.telerik.com/login
- group: start
  title: ''
  type: Signup
  url: https://www.telerik.com/login#register
- group: learn
  title: ''
  type: Videos
  url: https://www.youtube.com/c/progresssw
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/anthropaboroshi
created: '2026-03-26'
description: Fiddler by Telerik (Progress Software) is a suite of HTTP debugging proxy tools for capturing, inspecting, modifying, and replaying HTTP and HTTPS traffic between computers. The product family includes Fiddler Everywhere (cross-platform), Fiddler Classic (Windows), and Fiddler Jam (browser-based collaboration tool) for API debugging, performance testing, and web development workflows.
finops:
- name: Fiddler Finops
  service_category: API
  slug: fiddler-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/fiddler.png
layout: provider
modified: '2026-03-26'
name: Fiddler
nav: Providers
network: true
overview: 'Fiddler publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include API Debugging, HTTP Debugging, HTTP Proxy, Performance Testing, and Traffic Inspection.


  Fiddler''s developer surface includes documentation, engineering blog, pricing, support, signup flow, and 9 more developer resources.'
plans:
- name: Fiddler Plans Pricing
  plan_count: 3
  slug: fiddler-plans-pricing
random_paper: 16
rate_limits:
- limit_count: 5
  name: Fiddler Rate Limits
  slug: fiddler-rate-limits
score:
  band: emerging
  composite: 17.8
  delta: 0.0
  facets:
    access_clarity: 32.9
    commercial_clarity: 32.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 16.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  previous_composite: 17.8
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/fiddler/refs/heads/main/screenshots/fiddler-2026-06-20T181148.png
security:
- kind: domain-security
  name: Fiddler Domain Security
  slug: fiddler-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Fiddler Vulnerability Disclosure
  slug: fiddler-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: fiddler
tags:
- API Debugging
- HTTP Debugging
- HTTP Proxy
- Performance Testing
- Traffic Inspection
- Web Development
website: https://www.telerik.com/fiddler
---
