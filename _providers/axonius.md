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
    error_semantics: false
    event_surface_described: true
    idempotency: false
    mcp_server: documented
    openapi_examples: false
    protected_resource_metadata: false
    rate_limit_signal: documented
    reversibility_documented: false
    spec_presence: true
    well_known_catalog: false
  schema_version: '0.2'
  score: 25.8
  scored_at: '2026-09-23'
api_count: 1
apis:
- description: Axonius is a cybersecurity asset management platform providing SaaS management, device discovery, and security policy enforcement across IT environments.
  name: Axonius
  slug: axonius
artifact_total: 32
asyncapis:
- description: ''
  name: Axonius Webhooks
  slug: axonius-webhooks
collections:
- collection_type: postman
  name: activity logs
  slug: postman-axonius-activity-logs
- collection_type: postman
  name: custom data crud operations
  slug: postman-axonius-custom-data
- collection_type: postman
  name: dashboards, charts, queries - import/export
  slug: postman-axonius-dashboards-import-export
- collection_type: postman
  name: Devices
  slug: postman-axonius-devices
common:
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/security/axonius-trust-center.yml
  title: ''
  type: TrustCenter
  url: security/axonius-trust-center.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/security/axonius-domain-security.yml
  title: ''
  type: DomainSecurity
  url: security/axonius-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/axonius
- group: company
  title: ''
  type: Website
  url: https://www.axonius.com
- group: docs
  title: ''
  type: Documentation
  url: https://docs.axonius.com/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/Axonius
- group: company
  title: ''
  type: Blog
  url: https://www.axonius.com/blog
- group: commercial
  title: ''
  type: Pricing
  url: https://aws.amazon.com/marketplace/pp/prodview-bupmprfogelg4
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.axonius.com/legal/terms-conditions
- group: commercial
  title: ''
  type: PrivacyPolicy
  url: https://www.axonius.com/privacy-policy
- group: start
  title: ''
  type: GettingStarted
  url: https://docs.axonius.com/docs/axonius-rest-api
- group: start
  title: ''
  type: DeveloperPortal
  url: https://developer.axonius.com/
- group: docs
  title: ''
  type: APIReference
  url: https://developer.axonius.com/
- group: operate
  title: ''
  type: Support
  url: https://support.axonius.com/
- group: build
  title: ''
  type: Postman
  url: https://github.com/Axonius/postman-minis
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/packages/axonius-packages.yml
  title: ''
  type: Packages
  url: packages/axonius-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/packages/axonius-packages.yml
  title: ''
  type: SDKs
  url: packages/axonius-packages.yml
- group: build
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/cli/axonius-cli.yml
  title: ''
  type: CLI
  url: cli/axonius-cli.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/well-known/axonius-well-known.yml
  title: ''
  type: WellKnown
  url: well-known/axonius-well-known.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/well-known/axonius-security.txt
  title: ''
  type: SecurityTxt
  url: well-known/axonius-security.txt
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/security/axonius-vulnerability-disclosure.yml
  title: ''
  type: VulnerabilityDisclosure
  url: security/axonius-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/security/axonius-vulnerability-disclosure.yml
  title: ''
  type: Security
  url: security/axonius-vulnerability-disclosure.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/security/axonius-trust-center.yml
  title: ''
  type: Compliance
  url: security/axonius-trust-center.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/conformance/axonius-conformance.yml
  title: ''
  type: Conformance
  url: conformance/axonius-conformance.yml
- group: auth
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/authentication/axonius-authentication.yml
  title: ''
  type: Authentication
  url: authentication/axonius-authentication.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/mcp/axonius-mcp.yml
  title: ''
  type: MCPServer
  url: mcp/axonius-mcp.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/lifecycle/axonius-lifecycle.yml
  title: ''
  type: Lifecycle
  url: lifecycle/axonius-lifecycle.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/changelog/axonius-changelog.yml
  title: ''
  type: ChangeLog
  url: changelog/axonius-changelog.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/conventions/axonius-conventions.yml
  title: ''
  type: Conventions
  url: conventions/axonius-conventions.yml
- group: design
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/asyncapi/axonius-webhooks.yml
  title: ''
  type: Webhooks
  url: asyncapi/axonius-webhooks.yml
- group: commercial
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/plans/axonius-plans-pricing.yml
  title: ''
  type: Plans
  url: plans/axonius-plans-pricing.yml
- group: operate
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/rate-limits/axonius-rate-limits.yml
  title: ''
  type: RateLimits
  url: rate-limits/axonius-rate-limits.yml
- group: agent
  href: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/llms/axonius-llms.txt
  title: ''
  type: LLMsTxt
  url: llms/axonius-llms.txt
- group: agent
  title: ''
  type: LlmsText
  url: https://docs.axonius.com/llms.txt
created: '2026-03-27'
description: Axonius is a cybersecurity asset management platform (Axonius Asset Cloud) that aggregates device, user, cloud, SaaS and vulnerability data from 800+ adapters into one correlated inventory, enforces security policies through automated enforcement actions and workflows, and exposes that inventory over a service-account REST API (API v2), an Axonius Query Language, a deprecated Python client and CLI, outbound webhooks, and an early-access MCP server.
features:
- description: Automatically discover all devices, users, and cloud assets across the environment.
  name: Asset Discovery
- description: Manage SaaS application access, licenses, and security posture from a single platform.
  name: SaaS Management
- description: Enforce security policies across assets and trigger automated remediation workflows.
  name: Security Enforcement
- description: Connect to 800+ security and IT tools for data aggregation and correlation.
  name: Integration Hub
- description: Correlate vulnerability scanner data with asset context for prioritized remediation.
  name: Vulnerability Management
- description: Generate compliance reports for CIS Benchmarks, NIST, PCI DSS, and other frameworks.
  name: Compliance Reporting
- description: Build complex queries to find assets matching specific security criteria.
  name: Query Builder
- description: Track asset lifecycle from procurement to decommission with full audit trail.
  name: Lifecycle Management
finops:
- name: Axonius Finops
  service_category: API
  slug: axonius-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/axonius.png
integrations:
- description: Pull endpoint data from CrowdStrike Falcon to enrich asset inventory.
  name: CrowdStrike
- description: Sync user and device data from Active Directory and Azure AD.
  name: Microsoft Active Directory
- description: Push asset data and incidents to ServiceNow CMDB and ITSM.
  name: ServiceNow
- description: Correlate Qualys vulnerability scan data with asset context.
  name: Qualys
- description: Correlate SaaS user access data with identity from Okta.
  name: Okta
layout: provider
mcp_servers:
- description: 'Axonius announced the Axonius MCP Server on 2026-07-21 (blog + GlobeNewswire press release): it "translates natural language questions into Axonius Query Language (AQL) and returns live answers" acros'
  name: Axonius MCP Server
  slug: axonius-mcp-server
modified: '2026-09-18'
name: Axonius
nav: Providers
network: true
overview: 'Axonius publishes 1 API on the [APIs.io](https://apis.io/) network: Axonius. Tagged areas include Asset Management, Cybersecurity, SaaS Management, SaaS Security, and Vulnerability Management.


  The Axonius catalog on APIs.io includes 1 event-driven AsyncAPI specification.


  Axonius'' developer surface includes documentation, engineering blog, pricing, getting-started guide, API reference, support, CLI, and 27 more developer resources.'
plans:
- name: Axonius Plans Pricing
  plan_count: 2
  slug: axonius-plans-pricing
random_paper: 5
rate_limits:
- limit_count: 0
  name: Axonius Rate Limits
  slug: axonius-rate-limits
score:
  band: developing
  composite: 49.8
  coverage:
    artifact_dirs: 19
    catalog_earned: 48.0
    catalog_earned_first_party: 8.0
    catalog_gap: 67.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 65.8
    contract_governance: 18.2
    contract_quality: 41.6
    developer_ergonomics: 58.3
    discoverability: 75.9
    operational_transparency: 36.8
  previous_composite: 49.8
  provenance:
    conformance: first-party
    mcp: first-party
  schema_version: 0.22.0
  scored_at: '2026-09-23'
  trend: flat
  upsert:
    applies: false
    note: 'Not scored: no parseable contract to read. Never-measured is not the same fact as measured-empty, so this is absent rather than zero.'
    reason: no_specs
screenshot: https://raw.githubusercontent.com/api-evangelist/axonius/refs/heads/main/screenshots/axonius-2026-06-20T172834.png
security:
- kind: authentication
  name: Axonius Authentication
  slug: axonius-authentication
  summary_line: apiKey/oauth2 · 2 schemes
- kind: domain-security
  name: Axonius Domain Security
  slug: axonius-domain-security
  summary_line: TLSv1.3 · DMARC
- kind: vulnerability-disclosure
  name: Axonius Vulnerability Disclosure
  slug: axonius-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
- kind: trust-center
  name: Axonius Trust Center
  slug: axonius-trust-center
  summary_line: SOC 2, ISO 27001, HIPAA, FedRAMP, CSA STAR
slug: axonius
tags:
- Asset Management
- Cybersecurity
- SaaS Management
- SaaS Security
- Vulnerability Management
- IT Asset Management
- Security Operations
use_cases:
- description: Maintain a complete, always-accurate inventory of all IT and OT assets.
  name: Asset Inventory
- description: Identify unauthorized devices and SaaS applications in use across the organization.
  name: Shadow IT Discovery
- description: Enforce zero trust policies by continuously validating asset compliance.
  name: Zero Trust Security
- description: Quickly identify affected assets during security incidents for rapid containment.
  name: Incident Response
- description: Prove compliance with security frameworks using comprehensive asset data.
  name: Compliance Auditing
website: https://www.axonius.com
---
