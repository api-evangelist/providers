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
  scored_at: '2026-09-01'
api_count: 8
apis:
- description: RESTful interface for the nGeniusONE platform, enabling network performance monitoring, analytics, and service assurance automation.
  name: Netscout nGeniusONE API
  slug: ngeniusone
- description: REST API for DDoS detection, mitigation, and threat intelligence on the Arbor Sightline platform. Provides programmatic access to alerts, mitigations, routers, managed objects, and annotations via a J
  name: Netscout Arbor Sightline SP REST API
  slug: arbor-sightline
- description: Open API surface for the Omnis Cyber Intelligence NDR platform, enabling network investigation and adding network context to third-party alerts from SIEM and EDR systems using historical network metad
  name: Netscout Omnis Cyber Intelligence API
  slug: omnis-cyber-intelligence
- description: Programmatic interface to deep packet inspection data and network flow analytics from InfiniStreamNG appliances. Feeds ASI Smart Data metadata to analytics stacks for service assurance, application pe
  name: Netscout InfiniStreamNG API
  slug: infinistreamng
- description: REST API for Arbor Edge Defense (AED), an inline security appliance deployed at the network perimeter that provides stateless, on-premises DDoS protection. Enables programmatic management of inbound a
  name: Netscout Arbor Edge Defense API
  slug: arbor-edge-defense
- description: API for the Arbor Threat Mitigation System (TMS), the carrier-class DDoS mitigation solution that works with Arbor Sightline to surgically remove DDoS attack traffic from network flows. Provides progr
  name: Netscout Arbor Threat Mitigation System API
  slug: arbor-tms
- description: API surface for nGeniusPULSE, Netscout's synthetic testing and active monitoring platform. nGeniusPULSE uses nPoint test agents deployed across LAN, WAN, Wi-Fi, VPN, data centers, and cloud environmen
  name: Netscout nGeniusPULSE API
  slug: ngeniuspulse
- description: REST and Kafka interfaces for the nGenius Business Analytics platform, enabling service providers to export enriched ASI Smart Data to third-party data lakes, applications, and analytics platforms for
  name: Netscout nGenius Business Analytics API
  slug: ngenius-business-analytics
artifact_total: 14
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/arbor/aedansible/issues
- group: auth
  title: ''
  type: TrustCenter
  url: security/netscout-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/netscout-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/netscout-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/netscout
- group: start
  title: ''
  type: Portal
  url: https://my.netscout.com/Pages/overview.aspx
- group: docs
  title: ''
  type: Documentation
  url: https://www.netscout.com/resources
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.netscout.com/legal/terms-and-conditions
- group: commercial
  title: ''
  type: Website Terms of Use
  url: https://www.netscout.com/legal/website-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.netscout.com/legal/privacy-policy
- group: commercial
  title: ''
  type: Legal
  url: https://www.netscout.com/legal
- group: operate
  title: ''
  type: Contact
  url: https://www.netscout.com/contact-us
- group: company
  title: ''
  type: Blog
  url: https://www.netscout.com/blog
- group: operate
  title: ''
  type: Support
  url: https://www.netscout.com/support-services
- group: company
  title: ''
  type: Website
  url: https://www.netscout.com
- group: start
  title: ''
  type: Login
  url: https://my.netscout.com/Pages/overview.aspx
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/arbor
- group: auth
  title: ''
  type: Security
  url: https://www.netscout.com/data-privacy-and-trust-center
created: '2025-01-20'
description: Netscout provides service assurance, cybersecurity, and DDoS protection solutions. Their products enable network visibility, threat intelligence, and performance monitoring across hybrid and cloud environments. Several Netscout products expose REST APIs and integration interfaces for observability, security automation, and analytics workflows.
finops:
- name: Netscout Finops
  service_category: API
  slug: netscout-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/netscout.png
layout: provider
modified: '2026-04-28'
name: Netscout
nav: Providers
network: true
overview: 'Netscout publishes 8 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, DDoS Protection, Network Monitoring, Network Performance, and Service Assurance.


  Netscout''s developer surface includes developer portal, documentation, legal docs, engineering blog, support, and 13 more developer resources.'
plans:
- name: Netscout Plans Pricing
  plan_count: 3
  slug: netscout-plans-pricing
random_paper: 3
rate_limits:
- limit_count: 5
  name: Netscout Rate Limits
  slug: netscout-rate-limits
score:
  band: thin
  composite: 29.8
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 57.9
    commercial_clarity: 57.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 29.8
  schema_version: 0.18.0
  scored_at: '2026-09-01'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/netscout/refs/heads/main/screenshots/netscout-2026-06-20T190205.png
security:
- kind: domain-security
  name: Netscout Domain Security
  slug: netscout-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Netscout Vulnerability Disclosure
  slug: netscout-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Netscout Trust Center
  slug: netscout-trust-center
  summary_line: SOC 2, ISO 27001, ISO 27017, PCI DSS, GDPR
slug: netscout
tags:
- Cybersecurity
- DDoS Protection
- Network Monitoring
- Network Performance
- Service Assurance
- Threat Intelligence
website: https://www.netscout.com
---
