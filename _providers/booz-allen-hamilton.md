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
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: true
    agentic_access: false
    agentic_commerce: false
    auth_clarity: false
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: documented
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.2
  scored_at: '2026-09-18'
api_count: 1
apis:
- description: The HTTP and A2A surface of Booz Allen's Agent Foundry agent baseline, an Apache-2.0 composition root that teams fork and deploy in their own environment. It serves three REST groups — /api/v1/query (
  name: Agent Foundry — Strands Base Agent API
  slug: booz-allen-hamilton-agent-foundry-strands-base-agent
- baseURL: https://{agent-host}/api/v1
  baseurl_source: declared
  description: The agile API from Booz Allen Hamilton — 1 operation(s) for agile.
  name: Booz Allen Hamilton Agile API
  slug: booz-allen-hamilton-agile-api
artifact_total: 16
common:
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/overlays/booz-allen-hamilton-palm-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/booz-allen-hamilton-palm-overlay.yaml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/security/booz-allen-hamilton-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/booz-allen-hamilton-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/booz-allen-hamilton
- group: company
  title: ''
  type: Website
  url: https://www.boozallen.com
- group: build
  title: ''
  type: GitHub
  url: https://github.com/boozallen
- group: other
  title: ''
  type: X-OpenDataPlatform
  url: https://boozallen.github.io/opendataplatform/
- group: other
  title: ''
  type: X-SolutionsDeliveryPlatform
  url: https://boozallen.github.io/sdp-docs/overview/1/index.html
- group: company
  title: ''
  type: Blog
  url: https://www.boozallen.com/insights.html
- group: company
  title: ''
  type: About
  url: https://www.boozallen.com/about.html
- group: company
  title: ''
  type: Careers
  url: https://www.boozallen.com/careers.html
- group: operate
  title: ''
  type: Contact
  url: https://www.boozallen.com/tools/footer-navigation/contact-us.html
- group: agent
  title: ''
  type: LlmsText
  url: https://boozallen.com/llms.txt
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.boozallen.com/tools/footer-navigation/terms-of-use.html
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.boozallen.com/tools/footer-navigation/privacy-policy.html
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/packages/booz-allen-hamilton-packages.yml
  title: ''
  type: Packages
  url: packages/booz-allen-hamilton-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/packages/booz-allen-hamilton-packages.yml
  title: ''
  type: SDKs
  url: packages/booz-allen-hamilton-packages.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/conventions/booz-allen-hamilton-conventions.yml
  title: ''
  type: Conventions
  url: conventions/booz-allen-hamilton-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/conventions/booz-allen-hamilton-conventions.yml
  title: ''
  type: Idempotency
  url: conventions/booz-allen-hamilton-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/errors/booz-allen-hamilton-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/booz-allen-hamilton-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/data-model/booz-allen-hamilton-data-model.yml
  title: ''
  type: DataModel
  url: data-model/booz-allen-hamilton-data-model.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/lifecycle/booz-allen-hamilton-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/booz-allen-hamilton-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/changelog/booz-allen-hamilton-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/booz-allen-hamilton-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/conformance/booz-allen-hamilton-conformance.yml
  title: ''
  type: Conformance
  url: conformance/booz-allen-hamilton-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/conformance/booz-allen-hamilton-conformance.yml
  title: ''
  type: Compliance
  url: conformance/booz-allen-hamilton-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/security/booz-allen-hamilton-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/booz-allen-hamilton-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.boozallen.com/e/about-content/cyber-security-concern-reporting.html
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/mcp/booz-allen-hamilton-mcp.yml
  title: ''
  type: MCPClient
  url: mcp/booz-allen-hamilton-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/plans/booz-allen-hamilton-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/booz-allen-hamilton-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/rate-limits/booz-allen-hamilton-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/booz-allen-hamilton-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/well-known/booz-allen-hamilton-well-known.yml
  title: ''
  type: X-WellKnownProbe
  url: well-known/booz-allen-hamilton-well-known.yml
created: '2024-01-01'
description: Booz Allen Hamilton is a leading management and technology consulting firm providing services primarily to U.S. government agencies in defense, intelligence, and civil markets. The firm employs over 2,500 AI specialists and 8,000 cybersecurity professionals, and maintains a significant open source presence on GitHub with projects including the Solutions Delivery Platform, Open Data Platform, and Cognition data fusion platform.
features:
- features:
  - DevSecOps Pipeline
  - CI/CD Automation
  - Reusable Pipeline Framework
  - Open Source
  - Government DevOps
  name: Solutions Delivery Platform (SDP)
  url: https://boozallen.github.io/sdp-docs/overview/1/index.html
- features:
  - Enterprise Data Platform
  - Vendor Neutral
  - Open Source
  - Data Ingest
  - Data Management
  - Scalable Architecture
  name: Open Data Platform
  url: https://boozallen.github.io/opendataplatform/
- features:
  - Data Ingest
  - Data Fusion
  - Search
  - Open Source
  - Intelligence Analytics
  name: Cognition Platform
  url: https://github.com/boozallen/cognition
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/booz-allen-hamilton.png
layout: provider
modified: '2026-09-14'
name: Booz Allen Hamilton
nav: Providers
network: true
overview: 'Booz Allen Hamilton publishes 1 API on the [APIs.io](https://apis.io/) network: Agile API. Tagged areas include Artificial Intelligence, Consulting, Cybersecurity, Defense, and Federal-Government.


  Booz Allen Hamilton''s developer surface includes GitHub presence, engineering blog, changelog, and 28 more developer resources.'
plans:
- name: Booz Allen Hamilton Plans Pricing
  plan_count: 0
  slug: booz-allen-hamilton-plans-pricing
press:
- date: '2026-05-25'
  title: Press Releases | Booz Allen Hamilton Inc.
  url: https://newsroom.boozallen.com/press-releases?page=1
- date: '2026-05-25'
  title: INVESTOR NEWS | Booz Allen Hamilton
  url: https://investors.boozallen.com/press-releases
- date: '2026-05-25'
  title: Booz Allen Hamilton Holding (NYSE:BAH) Stock Price News
  url: https://stocklight.com/stocks/us/nyse-bah/booz-allen-hamilton-holding?media_id=181264
- date: '2026-05-25'
  title: Press Releases | Booz Allen Hamilton Inc.
  url: https://newsroom.boozallen.com/press-releases
- date: '2026-05-25'
  title: Booz Allen outlines tech strategy and key risks
  url: https://www.stocktitan.net/sec-filings/BAH/10-k-booz-allen-hamilton-holding-corp-files-annual-report-f81cdf47fedf.html
random_paper: 2
rate_limits:
- limit_count: 0
  name: Booz Allen Hamilton Rate Limits
  slug: booz-allen-hamilton-rate-limits
score:
  band: developing
  composite: 42.6
  coverage:
    artifact_dirs: 22
    catalog_earned: 37.0
    catalog_earned_first_party: 0.0
    catalog_gap: 78.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 28.9
    contract_governance: 18.2
    contract_quality: 38.1
    developer_ergonomics: 45.2
    discoverability: 75.9
    operational_transparency: 31.6
  previous_composite: 42.6
  provenance:
    conformance: first-party
    contracts:
      callable: 0.0
      derived: 0
      marker_coverage: 0.0
      total: 1
    mcp: derived
    skills: first-party
  regulatory:
    applies: true
    matched_via: tags
    regime: Government & Public Sector
    regime_id: government
    score: 55.6
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: true
    score: 0.0
screenshot: https://raw.githubusercontent.com/api-evangelist/booz-allen-hamilton/refs/heads/main/screenshots/booz-allen-hamilton-2026-06-20T173608.png
security:
- kind: authentication
  name: Booz Allen Hamilton Authentication
  slug: booz-allen-hamilton-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Booz Allen Hamilton Domain Security
  slug: booz-allen-hamilton-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Booz Allen Hamilton Vulnerability Disclosure
  slug: booz-allen-hamilton-vulnerability-disclosure
  summary_line: Hackerone
slug: booz-allen-hamilton
tags:
- Artificial Intelligence
- Consulting
- Cybersecurity
- Defense
- Federal-Government
- Intelligence
- Management Consulting
- Technology
- Fortune 500
use_cases:
- features:
  - AI Solutions
  - Machine Learning
  - Natural Language Processing
  - Computer Vision
  - LLM Integration
  - AI Governance
  - Federal AI
  name: Artificial Intelligence
  url: https://www.boozallen.com/expertise/analytics.html
- features:
  - Zero Trust Architecture
  - Threat Intelligence
  - Security Operations
  - Incident Response
  - Cyber Defense
  - Intelligence-Grade Security
  - Critical Infrastructure Protection
  name: Cybersecurity
  url: https://www.boozallen.com/expertise/cyber.html
- features:
  - Cloud Migration
  - Legacy Modernization
  - DevSecOps
  - Platform Engineering
  - Application Modernization
  - Digital Services
  name: Digital Transformation
  url: https://www.boozallen.com/expertise/digital.html
- features:
  - Warfighter Technology
  - C2 Systems
  - Mission Systems
  - Defense Analytics
  - Autonomous Systems
  name: Defense Technology
  url: https://www.boozallen.com/expertise/defense.html
- features:
  - Space Domain Awareness
  - Battle Management
  - Satellite Analytics
  - Space AI
  name: Space Technology
  url: https://www.boozallen.com/expertise/space.html
- features:
  - Quantum Algorithms
  - Quantum-Safe Cryptography
  - Quantum Sensing
  - Post-Quantum Security
  name: Quantum Computing
  url: https://www.boozallen.com/expertise/quantum.html
website: https://www.boozallen.com
---
