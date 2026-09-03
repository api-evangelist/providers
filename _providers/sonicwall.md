---
access_model:
  confidence: low
  label: Unknown
  onboarding: unknown
  pricing: unknown
  public: false
  source: []
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
    rate_limit_signal: false
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 0.0
  scored_at: '2026-09-03'
api_count: 0
artifact_total: 2
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/sonicwall-trust-center.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/sonicwall-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.sonicwall.com
- group: start
  title: ''
  type: Portal
  url: https://www.sonicwall.com/products
- group: docs
  title: ''
  type: Documentation
  url: https://www.sonicwall.com/support/technical-documentation
- group: docs
  title: ''
  type: Documentation
  url: https://www.sonicwall.com/support/technical-documentation/sonicwall-sonicos-api
- group: docs
  title: ''
  type: Documentation
  url: https://www.sonicwall.com/products/firewalls/security-services/capture-advanced-threat-protection
- group: docs
  title: ''
  type: Documentation
  url: https://www.sonicwall.com/products/cloud-secure-edge
- group: docs
  title: ''
  type: Documentation
  url: https://www.sonicwall.com/products/firewalls/virtual
- group: other
  title: ''
  type: Product
  url: https://www.sonicwall.com/products/firewalls/entry-level
- group: other
  title: ''
  type: Product
  url: https://www.sonicwall.com/products/firewalls/mid-range
- group: other
  title: ''
  type: Product
  url: https://www.sonicwall.com/products/firewalls/high-end
- group: operate
  title: ''
  type: Support
  url: https://www.sonicwall.com/support
- group: operate
  title: ''
  type: Community
  url: https://community.sonicwall.com/
- group: start
  title: ''
  type: Signup
  url: https://www.mysonicwall.com/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.sonicwall.com/
- group: auth
  title: ''
  type: SecurityAdvisory
  url: https://psirt.global.sonicwall.com/
- group: company
  title: ''
  type: Blog
  url: https://blog.sonicwall.com/en-us/
- group: other
  title: ''
  type: ThreatIntelligence
  url: https://securitynews.sonicwall.com/
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.sonicwall.com/legal/privacy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.sonicwall.com/legal/sonicwall-end-user-product-agreement
- group: auth
  title: ''
  type: TrustCenter
  url: https://www.sonicwall.com/legal
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/sonicwall
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/sonicwall
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/sonicwallinc
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/sonicwall
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sonicwall/sonicwall-capture-api-python
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sonicwall/sonicwall-capture-api-node
- group: build
  title: ''
  type: SDKs
  url: https://github.com/sonicwall/sonicwall-capture-api-php
- group: build
  title: ''
  type: Tools
  url: https://github.com/sonicwall/sonicos-automation
- group: build
  title: ''
  type: Tools
  url: https://github.com/sonicwall/sonicwall-captureclient-rmm
- group: build
  title: ''
  type: InfrastructureAsCode
  url: https://github.com/sonicwall/sonicwall-nsv-aws-cf-templates
- group: build
  title: ''
  type: InfrastructureAsCode
  url: https://github.com/sonicwall/sonicwall-nsv-azure-templates
- group: company
  title: ''
  type: Partners
  url: https://www.sonicwall.com/partners
- group: learn
  title: ''
  type: Training
  url: https://www.sonicwall.com/partners/sonicwall-university
created: '2026-05-25'
description: SonicWall is a Milpitas, California cybersecurity company that has been defending small and medium-sized businesses, enterprises, and managed service providers from cyber crime for more than 25 years. The company builds network security firewalls, secure access service edge (SASE) offerings, cloud email security, endpoint protection, and managed detection and response services. The SonicOS operating system that runs on TZ, NSa, NSsp, and NSv next-generation firewalls exposes an on-device REST API (SonicOS API) for configuration, monitoring, and policy management, but SonicWall does not publish a centralized OpenAPI specification — API documentation is shipped per SonicOS release as HTML and PDF reference manuals at sonicwall.com/support. SonicWall additionally operates the Capture Advanced Threat Protection (Capture ATP) cloud sandbox API and the Cloud Secure Edge (CSE) management surface, with reference SDKs in Node.js, Python, and PHP published in the github.com/sonicwall
  organization. The company also publishes CloudFormation and Azure Resource Manager templates for deploying NSv virtual firewalls. SonicWall's revenue model is firewall hardware sales, security service subscriptions, cloud security subscriptions, and managed services — there is no public consumer developer program or self-service signup for the firewall APIs (the SonicOS API is accessed against the customer's own firewall device).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/sonicwall.png
layout: provider
modified: '2026-05-25'
name: SonicWall
nav: Providers
network: true
overview: 'SonicWall is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Network Security, Firewall, Next-Generation Firewall, and Intrusion Prevention.


  SonicWall''s developer surface includes developer portal, documentation, support, signup flow, engineering blog, YouTube channel, tooling, and 28 more developer resources.'
random_paper: 6
score:
  band: emerging
  composite: 17.7
  coverage:
    artifact_dirs: 3
    catalog_gap: 88.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 21.1
    commercial_clarity: 21.1
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 40.5
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 17.7
  schema_version: 0.18.2
  scored_at: '2026-09-03'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/sonicwall/refs/heads/main/screenshots/sonicwall-2026-06-20T194209.png
security:
- kind: domain-security
  name: Sonicwall Domain Security
  slug: sonicwall-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: trust-center
  name: Sonicwall Trust Center
  slug: sonicwall-trust-center
  summary_line: SOC 2, FIPS 140
slug: sonicwall
tags:
- Cybersecurity
- Network Security
- Firewall
- Next-Generation Firewall
- Intrusion Prevention
- VPN
- SD-WAN
- SASE
- Cloud Secure Edge
- Zero Trust
- Endpoint Security
- Email Security
- Cloud Email Security
- Managed Detection and Response
- MSSP
- Sandbox
- Capture ATP
- SonicOS
- SMB
website: https://www.sonicwall.com
---
