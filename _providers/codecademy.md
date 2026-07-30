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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: false
    spec_presence: true
    well_known_catalog: false
  schema_version: 0.2
  score: 16.2
  scored_at: '2026-07-28'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/codecademy-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/codecademy-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.codecademy.com
- group: company
  title: ''
  type: About
  url: https://www.codecademy.com/about
- group: other
  title: ''
  type: Catalog
  url: https://www.codecademy.com/catalog
- group: commercial
  title: ''
  type: Pricing
  url: https://www.codecademy.com/pricing
- group: other
  title: ''
  type: Plus
  url: https://www.codecademy.com/plus
- group: other
  title: ''
  type: Pro
  url: https://www.codecademy.com/pro
- group: other
  title: ''
  type: Bootcamps
  url: https://www.codecademy.com/bootcamps
- group: company
  title: ''
  type: Careers
  url: https://www.codecademy.com/career-paths
- group: auth
  title: ''
  type: Certifications
  url: https://www.codecademy.com/certifications
- group: other
  title: ''
  type: Workspaces
  url: https://www.codecademy.com/workspaces
- group: docs
  title: ''
  type: Documentation
  url: https://www.codecademy.com/resources/docs
- group: company
  title: ''
  type: Blog
  url: https://www.codecademy.com/resources/blog
- group: other
  title: ''
  type: ForBusiness
  url: https://www.codecademy.com/business
- group: operate
  title: ''
  type: Help
  url: https://help.codecademy.com
- group: operate
  title: ''
  type: Status
  url: https://status.codecademy.com
- group: commercial
  title: ''
  type: Terms
  url: https://www.codecademy.com/policy/terms
- group: commercial
  title: ''
  type: Privacy
  url: https://www.codecademy.com/policy/privacy
- group: company
  title: ''
  type: Careers
  url: https://www.codecademy.com/about/careers
- group: company
  title: ''
  type: Press
  url: https://www.codecademy.com/about/press
- group: other
  title: ''
  type: ParentCompany
  url: https://www.skillsoft.com
- group: other
  title: ''
  type: AcquisitionAnnouncement
  url: https://www.skillsoft.com/press-releases/skillsoft-completes-acquisition-of-codecademy
- group: build
  title: ''
  type: GitHub
  url: https://github.com/Codecademy
- group: company
  title: ''
  type: Twitter
  url: https://twitter.com/Codecademy
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/codecademy
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/user/Codecademy
- group: company
  title: ''
  type: Facebook
  url: https://www.facebook.com/Codecademy
- group: company
  title: ''
  type: Instagram
  url: https://www.instagram.com/codecademy
- group: docs
  title: ''
  type: GraphQL
  url: graphql/codecademy-graphql.md
created: '2026-05-25'
description: Codecademy is a New York City–based online learning platform offering interactive coding tutorials, career paths, certifications, and bootcamps across programming languages, data science, AI, cloud computing, cybersecurity, and web development. Founded in 2011 by Zach Sims and Ryan Bubinski, the company built its reputation on browser-based interactive exercises that let learners write and execute code without local setup, and grew to serve millions of registered learners. Codecademy was acquired by Skillsoft in April 2022 for approximately 525 million dollars in a cash-and-stock deal, and now operates as the consumer- and individual- developer-facing brand within Skillsoft's broader corporate learning portfolio, complementing Skillsoft Percipio for enterprise customers. Codecademy's products include the free tier, Codecademy Plus, Codecademy Pro, career paths, skill paths, professional certifications, full cohort-based bootcamps (via Codecademy and Skillsoft's Global Knowledge
  arm), and a workspaces feature for project work. The company does not expose a public developer REST API, SDK, or partner API program for programmatic access to courses, progress, or learner data; its primary surface is the codecademy.com web application and mobile apps, with enterprise content delivery handled through Skillsoft channels.
graphqls:
- description: This GraphQL schema represents a conceptual model of the Codecademy online programming education platform. Codecademy provides interactive coding tutorials, career paths, certifications, and bootcamps
  name: Codecademy GraphQL Schema
  slug: codecademy-graphql
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/codecademy.png
layout: provider
modified: '2026-05-25'
name: Codecademy
nav: Providers
network: true
overview: 'Codecademy is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Education, Online Learning, Coding Tutorials, Bootcamps, and Developer Education.


  Codecademy''s developer surface includes pricing, documentation, engineering blog, status page, terms of service, privacy policy, GitHub presence, and 23 more developer resources.'
random_paper: 54
score:
  band: emerging
  composite: 24.1
  delta: 10.3
  facets:
    commercial_clarity: 21.1
    contract_quality: 48.1
    developer_ergonomics: 10.9
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 5.3
  previous_composite: 13.8
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: rising
screenshot: https://raw.githubusercontent.com/api-evangelist/codecademy/refs/heads/main/screenshots/codecademy-2026-06-20T174659.png
security:
- kind: domain-security
  name: Codecademy Domain Security
  slug: codecademy-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Codecademy Vulnerability Disclosure
  slug: codecademy-vulnerability-disclosure
  summary_line: Hackerone · security.txt · contact published
slug: codecademy
tags:
- Education
- Online Learning
- Coding Tutorials
- Bootcamps
- Developer Education
- Career Paths
- Certifications
- Skillsoft
- EdTech
- Workforce Development
website: https://www.codecademy.com
---
