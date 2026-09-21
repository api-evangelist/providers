---
access_model:
  confidence: medium
  label: Freemium
  onboarding: unknown
  pricing: freemium
  public: false
  source:
  - pricing
  - docs
  trial: true
  try_now: false
agent_readiness:
  band: agent-ready
  dimensions:
    agent_card: false
    agent_skills: derived
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
    consent_identity: false
    delegated_identity: false
    dry_run_mode: na
    dynamic_client_registration: false
    error_semantics: documented
    event_surface_described: false
    idempotency: na
    mcp_server: false
    openapi_examples: verified
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: na
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 31.0
  scored_at: '2026-09-20'
api_count: 1
apis:
- description: Augmentt Discover provides SaaS discovery and Shadow IT detection capabilities for MSPs, identifying all cloud applications used across managed client environments.
  name: Augmentt Discover
  slug: augmentt-discover
- description: Augmentt Optimize tracks SaaS usage and spend across client environments to identify unused licenses, redundant applications, and cost savings opportunities for MSPs.
  name: Augmentt Optimize
  slug: augmentt-optimize
- description: Augmentt Engage provides SaaS administration, management, and automation capabilities allowing MSPs to centralize SaaS security policy enforcement and user lifecycle management across Microsoft 365 an
  name: Augmentt Engage
  slug: augmentt-engage
- baseURL: https://api.augmentt.com
  baseurl_source: declared
  description: Companies (tenants) configured under Configuration > Companies in the Augmentt portal.
  name: Augmentt Customers API
  slug: augmentt-customers-api
- baseURL: https://api.augmentt.com
  baseurl_source: declared
  description: Augmentt module license consumption and Microsoft 365 licensing reports.
  name: Augmentt Licensing API
  slug: augmentt-licensing-api
- baseURL: https://api.augmentt.com
  baseurl_source: declared
  description: MFA, security posture, threat and summary reporting for managed tenants.
  name: Augmentt Security Reports API
  slug: augmentt-security-reports-api
artifact_total: 26
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/security/augmentt-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/augmentt-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/security/augmentt-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/augmentt-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Augmentt
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/augmentt
- group: company
  title: ''
  type: Website
  url: https://www.augmentt.com
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.augmentt.com/privacy-policy/
- group: operate
  title: ''
  type: Contact
  url: https://www.augmentt.com/contact/
- group: company
  title: ''
  type: Blog
  url: https://www.augmentt.com/blog/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.augmentt.com/pricing/
- group: docs
  title: ''
  type: Documentation
  url: https://support.augmentt.com/kb/en
- group: start
  title: ''
  type: DeveloperPortal
  url: https://support.augmentt.com/kb/en/augmentt-api-548051
- group: docs
  title: ''
  type: APIReference
  url: https://support.augmentt.com/kb/en/augmentt-api-548051
- group: start
  title: ''
  type: GettingStarted
  url: https://support.augmentt.com/kb/en/getting-started-548027
- group: operate
  title: ''
  type: Support
  url: https://support.augmentt.com/kb/en/submit-a-support-ticket-377576
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.augmentt.com/subscription-agreement/
- group: start
  title: ''
  type: SignUp
  url: https://www.augmentt.com/free-sign-up/
- group: operate
  title: ''
  type: Roadmap
  url: https://www.augmentt.com/product-roadmap/
- group: operate
  title: ''
  type: StatusPage
  url: https://status.augmentt.com/
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/lifecycle/augmentt-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/augmentt-lifecycle.yml
- group: operate
  title: ''
  type: ChangeLog
  url: https://www.augmentt.com/blog/category/product/
- group: auth
  title: ''
  type: Security
  url: https://www.augmentt.com/responsible-disclosure-policy/
- group: auth
  title: ''
  type: TrustCenter
  url: https://trust.augmentt.com/
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/security/augmentt-trust-center.yml
  title: ''
  type: Compliance
  url: security/augmentt-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/conformance/augmentt-conformance.yml
  title: ''
  type: Conformance
  url: conformance/augmentt-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/authentication/augmentt-authentication.yml
  title: ''
  type: Authentication
  url: authentication/augmentt-authentication.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/errors/augmentt-problem-types.yml
  title: ''
  type: ErrorCatalog
  url: errors/augmentt-problem-types.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/conventions/augmentt-conventions.yml
  title: ''
  type: Conventions
  url: conventions/augmentt-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/data-model/augmentt-data-model.yml
  title: ''
  type: DataModel
  url: data-model/augmentt-data-model.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/packages/augmentt-packages.yml
  title: ''
  type: Packages
  url: packages/augmentt-packages.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/rate-limits/augmentt-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/augmentt-rate-limits.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/plans/augmentt-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/augmentt-plans-pricing.yml
- group: other
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/overlays/augmentt-api-overlay.yaml
  title: ''
  type: Overlay
  url: overlays/augmentt-api-overlay.yaml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/mcp/augmentt-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/augmentt-mcp.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/skills/_index.yml
  title: ''
  type: AgentSkill
  url: skills/_index.yml
- group: agent
  title: ''
  type: LLMsTxt
  url: https://augmentt.com/llms.txt
- group: company
  title: ''
  type: Careers
  url: https://www.augmentt.com/careers/
- group: company
  title: ''
  type: Newsroom
  url: https://www.augmentt.com/newsroom/
created: '2026-03-27'
description: Augmentt is a Canadian software company (Kanata, Ontario) whose platform gives managed service providers one place to run Microsoft 365 across every client tenant. It combines SaaS and Shadow IT discovery, Microsoft 365 license and spend optimization, user lifecycle automation, Intune device baselines, and a framework-mapped security posture engine that measures each tenant against CIS Microsoft 365 Foundations, CISA SCuBA, NIST CSF 2.0, Essential Eight, CMMC and HIPAA. It integrates with the PSA and RMM tools MSPs already run, including ConnectWise and N-able, and is distributed through the Pax8 marketplace. Augmentt publishes a read-only reporting API - twelve GET endpoints across three regional hosts - that lets partners pull customer, license, MFA, posture, threat and summary report data into their own BI, PSA or billing systems.
features:
- description: Manage SaaS applications across multiple client tenants from a single MSP dashboard with hierarchical access control.
  name: Multi-Tenant Management
- description: Automatically discover all cloud applications in use across client environments including Shadow IT not approved by IT.
  name: SaaS Discovery
- description: Track license utilization, identify unused seats, and generate recommendations to reduce SaaS spend across clients.
  name: License Optimization
- description: Enforce security policies across SaaS applications including MFA requirements, conditional access, and app permissions.
  name: SaaS Security Policies
- description: Automate user onboarding and offboarding across SaaS applications when employees join or leave client organizations.
  name: User Lifecycle Management
- description: Integrate discovery and optimization data with PSA platforms for automated billing and service delivery.
  name: PSA Integration
finops:
- name: Augmentt Finops
  service_category: API
  slug: augmentt-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/augmentt.png
layout: provider
mcp_servers:
- description: ''
  name: Augmentt MCP Server
  slug: augmentt-mcp-server
modified: '2026-09-14'
name: Augmentt
nav: Providers
network: true
overview: 'Augmentt publishes 3 APIs on the [APIs.io](https://apis.io/) network: Customers API, Licensing API, and Security Reports API. Tagged areas include MSP, Microsoft-365, SaaS Management, SaaS Security, and Shadow IT.


  Augmentt''s developer surface includes engineering blog, pricing, documentation, API reference, getting-started guide, support, signup flow, and 30 more developer resources.'
plans:
- name: Augmentt Plans Pricing
  plan_count: 5
  slug: augmentt-plans-pricing
random_paper: 11
rate_limits:
- limit_count: 0
  name: Augmentt Rate Limits
  slug: augmentt-rate-limits
score:
  band: developing
  composite: 43.0
  coverage:
    artifact_dirs: 21
    catalog_earned: 52.0
    catalog_earned_first_party: 12.0
    catalog_gap: 63.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 100.0
    contract_governance: 0.0
    contract_quality: 15.0
    developer_ergonomics: 25.6
    discoverability: 75.9
    operational_transparency: 50.0
  previous_composite: 43.0
  provenance:
    conformance: first-party
    contracts:
      callable: 100.0
      derived: 3
      marker_coverage: 100.0
      total: 3
    mcp: derived
    skills: derived
  schema_version: 0.22.0
  scored_at: '2026-09-20'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: this provider''s published contracts declare no write operations, and a read-only API cannot create-or-update. Excluded from the denominator, not zeroed.'
    reason: read_only
screenshot: https://raw.githubusercontent.com/api-evangelist/augmentt/refs/heads/main/screenshots/augmentt-2026-07-25T201708.png
security:
- kind: authentication
  name: Augmentt Authentication
  slug: augmentt-authentication
  summary_line: 0 schemes
- kind: domain-security
  name: Augmentt Domain Security
  slug: augmentt-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Augmentt Vulnerability Disclosure
  slug: augmentt-vulnerability-disclosure
  summary_line: Hackerone
- kind: trust-center
  name: Augmentt Trust Center
  slug: augmentt-trust-center
  summary_line: SOC 2 Type 2, GDPR
slug: augmentt
solutions:
- description: Package and deliver SaaS management as a managed service offering including discovery, optimization, and security monitoring.
  name: MSP SaaS Management Service
- description: Extend M365 security posture management with SaaS-specific controls, policy enforcement, and compliance reporting.
  name: Microsoft 365 Security
tags:
- MSP
- Microsoft-365
- SaaS Management
- SaaS Security
- Shadow IT
- Security Posture
- Compliance
- License Management
- Multi-Tenant
- Reporting
use_cases:
- description: Identify and eliminate wasted SaaS spend by discovering unused licenses and redundant applications across client portfolios.
  name: SaaS Spend Management
- description: Detect and manage unsanctioned cloud applications to reduce security risk and enforce acceptable use policies.
  name: Shadow IT Control
- description: Manage M365 licenses, security settings, and user access across all client tenants from a unified MSP console.
  name: Microsoft 365 Management
- description: Automate secure offboarding of departing employees by revoking access to all SaaS applications simultaneously.
  name: Employee Offboarding
website: https://www.augmentt.com
---
