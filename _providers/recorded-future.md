---
access_model:
  confidence: medium
  label: Free
  onboarding: unknown
  pricing: free
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
  scored_at: '2026-09-02'
api_count: 1
apis:
- description: The Recorded Future Intelligence Cloud REST API (api.recordedfuture.com) provides programmatic access to threat intelligence sourced from over a million open-web, dark-web, technical, and customer fee
  name: Recorded Future Intelligence Cloud API
  slug: recorded-future-connect-api
artifact_total: 31
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/recorded-future-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/recorded-future-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/recorded-future
- group: company
  title: ''
  type: Website
  url: https://www.recordedfuture.com/
- group: start
  title: Recorded Future Customer Portal
  type: Portal
  url: https://app.recordedfuture.com/
- group: operate
  title: ''
  type: Support
  url: https://support.recordedfuture.com/hc/en-us
- group: docs
  title: ''
  type: Documentation
  url: https://support.recordedfuture.com/hc/en-us
- group: company
  title: ''
  type: Blog
  url: https://www.recordedfuture.com/blog
- group: company
  title: The Record by Recorded Future
  type: News
  url: https://therecord.media/
- group: other
  title: ''
  type: CyberDaily
  url: https://www.recordedfuture.com/products/cyber-daily
- group: operate
  title: ''
  type: ContactSales
  url: https://www.recordedfuture.com/contact
- group: company
  title: ''
  type: Careers
  url: https://www.recordedfuture.com/careers
- group: company
  title: ''
  type: Partners
  url: https://www.recordedfuture.com/partners
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.recordedfuture.com/legal/privacy-policy
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.recordedfuture.com/legal/terms-of-service
created: '2026-05-23'
description: Recorded Future is a threat intelligence platform whose Intelligence Cloud combines open-web, dark-web, technical, and customer telemetry sources via the Intelligence Graph, indexed and analyzed by Insikt Group analysts and AI. The platform spans Threat Intelligence, Brand Intelligence, Identity Intelligence, SecOps Intelligence, Vulnerability Intelligence, Attack Surface Intelligence, Payment Fraud Intelligence, and Geopolitical Intelligence, plus Cyber Daily and the AI Analyst. Recorded Future exposes a REST API at api.recordedfuture.com (commonly called ConnectAPI) that customers and integration partners use to pull indicators, entities, alerts, and risk scores into SIEMs, SOARs, TIPs, and custom security workflows. Named a Leader in the 2026 Gartner Magic Quadrant for Cyberthreat Intelligence Technologies.
features:
- description: Unified intelligence platform delivering prioritized, organization-specific intelligence
  name: Intelligence Cloud
- description: Core graph data structure indexing and analyzing 1M+ open-web, dark-web, technical, and telemetry sources
  name: Intelligence Graph
- description: Tactical, operational, and strategic threat intelligence on actors, malware, TTPs, and indicators
  name: Threat Intelligence
- description: Detection of brand impersonation, typosquatting, and digital risk to corporate brands
  name: Brand Intelligence
- description: Monitoring of leaked credentials, identity exposures, and credential compromise events
  name: Identity Intelligence
- description: Intelligence purpose-built for SOC workflows, alerting, and triage
  name: SecOps Intelligence
- description: Vulnerability risk scoring, exploit chatter, and prioritization for patching decisions
  name: Vulnerability Intelligence
- description: Continuous discovery and monitoring of external-facing assets and exposures
  name: Attack Surface Intelligence
- description: Intelligence on stolen cards, fraud actors, and dark-web payment fraud markets
  name: Payment Fraud Intelligence
- description: Geopolitical and physical security intelligence for global operations
  name: Geopolitical Intelligence
- description: Generative AI assistant that summarizes intelligence and accelerates analyst workflows
  name: AI Analyst
- description: Daily curated digest of the global threat landscape
  name: Cyber Daily
- description: In-house intelligence research and analyst team producing finished intelligence
  name: Insikt Group
finops:
- name: Recorded Future Finops
  service_category: API
  slug: recorded-future-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/recorded-future.png
integrations:
- description: Out-of-the-box integrations with Splunk, Microsoft Sentinel, Google Chronicle, IBM QRadar, and others
  name: SIEM
- description: Playbook content and integrations for Cortex XSOAR, Splunk SOAR, Tines, Torq, and similar platforms
  name: SOAR
- description: Integrations with ThreatConnect, Anomali, and other Threat Intelligence Platforms
  name: TIP
- description: IOC feeds and blocklists for next-gen firewalls and secure web gateways
  name: Firewalls and Proxies
- description: Enrichment integrations with CrowdStrike, Microsoft Defender, SentinelOne, and others
  name: Endpoint and EDR
- description: Recorded Future browser extension surfaces intelligence in any web-based security tool
  name: Browser Extension
layout: provider
modified: '2026-05-23'
name: Recorded Future
nav: Providers
network: true
overview: 'Recorded Future publishes 1 API on the [APIs.io](https://apis.io/) network. Tagged areas include Cybersecurity, Threat Intelligence, Intelligence Cloud, Brand Intelligence, and Identity Intelligence.


  Recorded Future''s developer surface includes developer portal, support, documentation, engineering blog, product news, and 10 more developer resources.'
plans:
- name: Recorded Future Plans Pricing
  plan_count: 1
  slug: recorded-future-plans-pricing
random_paper: 19
rate_limits:
- limit_count: 2
  name: Recorded Future Rate Limits
  slug: recorded-future-rate-limits
score:
  band: emerging
  composite: 22.7
  coverage:
    artifact_dirs: 6
    catalog_gap: 59.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 39.5
    commercial_clarity: 39.5
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 26.2
    discoverability: 68.5
    governance: 0.0
    operational_transparency: 21.1
  previous_composite: 22.7
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/recorded-future/refs/heads/main/screenshots/recorded-future-2026-06-20T192704.png
security:
- kind: domain-security
  name: Recorded Future Domain Security
  slug: recorded-future-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Recorded Future Vulnerability Disclosure
  slug: recorded-future-vulnerability-disclosure
  summary_line: Bugcrowd · security.txt · contact published
slug: recorded-future
tags:
- Cybersecurity
- Threat Intelligence
- Intelligence Cloud
- Brand Intelligence
- Identity Intelligence
- Vulnerability Intelligence
- AI Analyst
use_cases:
- description: Enrich SIEM and SOAR alerts with risk scores and entity context from the Intelligence Cloud
  name: SOC Alert Triage
- description: Prioritize CVE remediation using real-world exploit and threat-actor activity
  name: Vulnerability Management
- description: Detect and respond to brand impersonation, typosquatting, and phishing infrastructure
  name: Brand Protection
- description: Detect leaked credentials and identity exposures for employees and customers
  name: Identity and Credential Monitoring
- description: Monitor third-party and supply-chain partners for threat exposure
  name: Third-Party Risk
- description: Track geopolitical events affecting people, facilities, and operations
  name: Geopolitical Risk
website: https://www.recordedfuture.com/
---
