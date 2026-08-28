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
    agent_skills: false
    agentic_access: false
    agentic_commerce: false
    auth_clarity: bearer
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
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 15.5
  scored_at: '2026-08-26'
api_count: 4
apis:
- description: REST API for managing candidates, contacts, clients, job openings, interviews, attachments, notes, and custom modules in Zoho Recruit. Requests are authenticated with OAuth 2.0 tokens issued by the do
  name: Zoho Recruit REST API v2
  slug: rest-api-v2
- description: The Candidates API from Zoho Recruit — 1 operation(s) for candidates.
  name: Zoho Recruit Candidates API
  slug: zoho-recruit-candidates-api
- description: The Job Openings API from Zoho Recruit — 1 operation(s) for job openings.
  name: Zoho Recruit Job Openings API
  slug: zoho-recruit-job-openings-api
- description: The Zoho Recruit API API from Zoho Recruit — 1 operation(s) for zoho recruit api.
  name: Zoho Recruit Zoho Recruit API API
  slug: zoho-recruit-zoho-recruit-api-api
artifact_total: 10
collections:
- collection_type: open
  name: API Collection
  slug: open-.refine-report
- collection_type: open
  name: Zoho Recruit Candidates API
  slug: open-zoho-recruit-candidates-api
- collection_type: open
  name: Zoho Recruit Job Openings API
  slug: open-zoho-recruit-job-openings-api
- collection_type: open
  name: Zoho Recruit Zoho Recruit API API
  slug: open-zoho-recruit-zoho-recruit-api-api
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/zoho-recruit-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/zoho-recruit-domain-security.yml
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/zoho
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/zohorecruit
- group: company
  title: ''
  type: Website
  url: https://www.zoho.com/recruit/
- group: docs
  title: ''
  type: Documentation
  url: https://www.zoho.com/recruit/developer-guide/apiv2/
- group: commercial
  title: ''
  type: Pricing
  url: https://www.zoho.com/recruit/zoho-recruit-pricing.html
- group: start
  title: ''
  type: Signup
  url: https://www.zoho.com/recruit/signup.html
- group: company
  title: ''
  type: Blog
  url: https://www.zoho.com/recruit/blog/feed/
created: '2026-05-11'
description: Zoho Recruit is an end-to-end applicant tracking system (ATS) and recruitment CRM for staffing agencies, corporate HR teams, and recruiters, covering job posting, candidate sourcing, interview scheduling, and hiring workflows. The Zoho Recruit v2 REST API exposes candidates, contacts, clients, jobs, interviews, and custom modules for full programmatic recruiting integrations. Authentication uses Zoho OAuth 2.0 with domain-specific endpoints (.com, .eu, .in, .com.au, .com.cn, .jp).
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/zoho-recruit.png
layout: provider
modified: '2026-05-11'
name: Zoho Recruit
nav: Providers
network: true
overview: 'Zoho Recruit publishes 3 APIs on the [APIs.io](https://apis.io/) network: Candidates API, Job Openings API, and Zoho Recruit API API. Tagged areas include ATS, Recruiting, Recruitment CRM, HR, and Zoho.


  Zoho Recruit''s developer surface includes documentation, pricing, signup flow, engineering blog, and 5 more developer resources.'
random_paper: 20
score:
  band: thin
  composite: 27.7
  delta: 2.0
  facets:
    access_clarity: 13.2
    commercial_clarity: 13.2
    contract_governance: 0.0
    contract_quality: 51.7
    developer_ergonomics: 11.9
    discoverability: 74.1
    governance: 0.0
    operational_transparency: 18.4
  previous_composite: 25.7
  provenance:
    contracts:
      callable: 100.0
      derived: 0
      marker_coverage: 0.0
      total: 3
  schema_version: 0.15.0
  scored_at: '2026-08-26'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/zoho-recruit/refs/heads/main/screenshots/zoho-recruit-2026-06-20T201945.png
security:
- kind: domain-security
  name: Zoho Recruit Domain Security
  slug: zoho-recruit-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Zoho Recruit Vulnerability Disclosure
  slug: zoho-recruit-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: zoho-recruit
tags:
- ATS
- Recruiting
- Recruitment CRM
- HR
- Zoho
website: https://www.zoho.com/recruit/
---
