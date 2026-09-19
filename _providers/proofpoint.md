---
agent_readiness:
  band: agent-aware
  dimensions:
    agent_card: false
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: false
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: false
    well_known_catalog: false
  schema_version: '0.2'
  score: 7.9
  scored_at: '2026-09-18'
api_count: 7
apis:
- description: 'The TAP v2 API exposes the Threat Insight Dashboard to machines: SIEM event download (blocked/permitted clicks, blocked/delivered messages, issues, all), campaign identifiers and detail, forensic evid'
  name: Proofpoint Targeted Attack Protection (TAP) API v2
  slug: proofpoint-tap
- description: The Dashboard Reports API returns the same executive-summary, effectiveness, people, organization and threat-landscape report cards the Threat Protection dashboard renders, plus mail-bomb (email bomb)
  name: Proofpoint Threat Protection Dashboard Reports API v1
  slug: proofpoint-threat-protection-reports
- description: The ET Intelligence Query API is Proofpoint's threat-intelligence lookup service, reached at api.emergingthreats.net. Thirty-six documented GET endpoints pivot across domains, IP addresses, malware sa
  name: Emerging Threats (ET) Intelligence Query API v1
  slug: proofpoint-et-intelligence
- description: 'The Results API exports Security Awareness Training outcomes for business-intelligence and LMS integration: CyberStrength knowledge assessments, PhishAlarm reports, ThreatSim simulated-phishing events'
  name: Proofpoint Security Awareness Training (ZenGuide) Results API
  slug: proofpoint-psat-results
- description: Secure Email Relay lets applications send authenticated transactional mail through Proofpoint rather than through an unmanaged relay, which is what makes a strict DMARC policy achievable. The Email Su
  name: Proofpoint Secure Email Relay (SER) Email Submission API
  slug: proofpoint-secure-email-relay
- description: Proofpoint Essentials — the SMB and MSP edition of the platform — exposes the same /v2/siem shape as TAP on its own regional hosts, returning blocked and permitted clicks and blocked and delivered mes
  name: Proofpoint Essentials Threat (SIEM) API
  slug: proofpoint-essentials-siem
- description: 'The PoD Log API is Proofpoint''s streaming surface rather than a request/response one: a client opens a WebSocket to logstream.proofpoint.com and subscribes to either the filter (message) log or the MT'
  name: Proofpoint on Demand (PoD) Log API
  slug: proofpoint-pod-log
artifact_total: 13
common:
- group: company
  title: ''
  type: Website
  url: https://www.proofpoint.com/us
- group: start
  title: ''
  type: DeveloperPortal
  url: https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation
- group: docs
  title: ''
  type: Documentation
  url: https://help.proofpoint.com/Threat_Insight_Dashboard/API_Documentation
- group: docs
  title: ''
  type: APIReference
  url: https://apidocs.emergingthreats.net/
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.proofpoint.com/us/legal/api-terms-of-use
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.proofpoint.com/us/legal/privacy-policy
- group: company
  title: ''
  type: Blog
  url: https://www.proofpoint.com/us/blog
- group: operate
  title: ''
  type: Support
  url: https://www.proofpoint.com/us/support-services
- group: operate
  title: ''
  type: Community
  url: https://proofpoint.my.site.com/community/s/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/pfptcommunity
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/packages/proofpoint-packages.yml
  title: ''
  type: Packages
  url: packages/proofpoint-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/packages/proofpoint-packages.yml
  title: ''
  type: SDKs
  url: packages/proofpoint-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/cli/proofpoint-cli.yml
  title: ''
  type: CLI
  url: cli/proofpoint-cli.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/authentication/proofpoint-authentication.yml
  title: ''
  type: Authentication
  url: authentication/proofpoint-authentication.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/rate-limits/proofpoint-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/proofpoint-rate-limits.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/errors/proofpoint-error-codes.yml
  title: ''
  type: ErrorCatalog
  url: errors/proofpoint-error-codes.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/conventions/proofpoint-conventions.yml
  title: ''
  type: Conventions
  url: conventions/proofpoint-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/lifecycle/proofpoint-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/proofpoint-lifecycle.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/conformance/proofpoint-conformance.yml
  title: ''
  type: Conformance
  url: conformance/proofpoint-conformance.yml
- group: auth
  title: ''
  type: Compliance
  url: https://www.proofpoint.com/us/legal/trust/product-certifications
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/security/proofpoint-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/proofpoint-trust-center.yml
- group: auth
  title: ''
  type: Trust
  url: https://www.proofpoint.com/us/legal/trust
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/security/proofpoint-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/proofpoint-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: Security
  url: https://www.proofpoint.com/us/security/vulnerability-disclosure-policy
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/security/proofpoint-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/proofpoint-domain-security.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/plans/proofpoint-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/proofpoint-plans-pricing.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/data-model/proofpoint-data-model.yml
  title: ''
  type: DataModel
  url: data-model/proofpoint-data-model.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/proofpoint/refs/heads/main/llms/proofpoint-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/proofpoint-llms.txt
created: '2026-09-13'
description: 'Proofpoint is an enterprise cybersecurity company focused on human-centric security — email and collaboration security, data loss prevention, insider threat management, digital communications governance, security awareness training and threat intelligence. Its public API surface is substantial but gateway-shaped rather than developer-portal-shaped: the Targeted Attack Protection (TAP) v2 API, the Threat Protection dashboard Reports API, the Emerging Threats (ET) Intelligence Query API, the ZenGuide / Security Awareness Training Results API, the Secure Email Relay email submission API, the Proofpoint Essentials SIEM API and the Proofpoint on Demand (PoD) log stream. Every one of them is documented in public HTML and every one of them is credential-gated at runtime; Proofpoint publishes no OpenAPI, AsyncAPI, GraphQL or MCP contract for any of them.'
image: https://kinlane-productions2.s3.amazonaws.com/api-evangelist-site/company-logos/proofpoint.png
layout: provider
modified: '2026-09-13'
name: Proofpoint
nav: Providers
network: true
overview: 'Proofpoint publishes 7 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Security, Cybersecurity, Email Security, Threat Intelligence, and Data Loss Prevention.


  Proofpoint''s developer surface includes documentation, API reference, engineering blog, support, CLI, authentication, and 22 more developer resources.'
plans:
- name: Proofpoint Plans Pricing
  plan_count: 0
  slug: proofpoint-plans-pricing
random_paper: 4
rate_limits:
- limit_count: 14
  name: Proofpoint Rate Limits
  slug: proofpoint-rate-limits
score:
  band: thin
  composite: 30.6
  coverage:
    artifact_dirs: 17
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 35.5
    contract_governance: 18.2
    contract_quality: 0.0
    developer_ergonomics: 44.0
    discoverability: 74.1
    operational_transparency: 39.5
  previous_composite: 30.6
  provenance:
    conformance: first-party
    mcp: derived
  schema_version: 0.22.0
  scored_at: '2026-09-18'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
security:
- kind: authentication
  name: Proofpoint Authentication
  slug: proofpoint-authentication
  summary_line: 5 schemes
- kind: domain-security
  name: Proofpoint Domain Security
  slug: proofpoint-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Proofpoint Vulnerability Disclosure
  slug: proofpoint-vulnerability-disclosure
  summary_line: Hackerone · contact published
- kind: trust-center
  name: Proofpoint Trust Center
  slug: proofpoint-trust-center
  summary_line: ISO/IEC 42001, ISO/IEC 27001, SOC 2, FedRAMP, IRAP, ENS (Esquema Nacional de Seguridad), EU-U.S. / UK Extension / Swiss-U.S. Data Privacy Framework, PCI DSS, FIPS 140 validated cryptographic modules, CSA STAR Registry
slug: proofpoint
tags:
- Security
- Cybersecurity
- Email Security
- Threat Intelligence
- Data Loss Prevention
- Security Awareness Training
- Insider Threat
- SIEM
- Compliance
- Email
website: https://www.proofpoint.com/us
---
