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
  scored_at: '2026-09-04'
api_count: 0
artifact_total: 3
common:
- group: auth
  title: ''
  type: TrustCenter
  url: security/alice-tech-trust-center.yml
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/alice-tech-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/alice-tech-domain-security.yml
- group: company
  title: ''
  type: Website
  url: https://www.alicetechnologies.com
- group: other
  title: ''
  type: Product
  url: https://www.alicetechnologies.com/construction-project-scheduling-software
- group: other
  title: ''
  type: ALICEOptimize
  url: https://www.alicetechnologies.com/alice-optimize
- group: commercial
  title: ''
  type: ALICEPlan
  url: https://www.alicetechnologies.com/alice-plan
- group: other
  title: ''
  type: ALICEModel
  url: https://www.alicetechnologies.com/alice-model
- group: other
  title: ''
  type: InsightsAgent
  url: https://www.alicetechnologies.com/construction-schedule-insights-agent
- group: other
  title: ''
  type: Company
  url: https://www.alicetechnologies.com/about
- group: start
  title: ''
  type: Demo
  url: https://www.alicetechnologies.com/alice-demo
- group: company
  title: ''
  type: Careers
  url: https://www.alicetechnologies.com/careers-2
- group: operate
  title: ''
  type: Support
  url: https://support.alicetechnologies.com
- group: company
  title: ''
  type: Blog
  url: https://blog.alicetechnologies.com
- group: other
  title: ''
  type: CaseStudies
  url: https://blog.alicetechnologies.com/case-studies
- group: company
  title: ''
  type: News
  url: https://blog.alicetechnologies.com/news
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/alicetechnologies
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/alice-technologies
- group: learn
  title: ''
  type: YouTube
  url: https://www.youtube.com/@alicetechnologies
created: '2026-05-25'
description: ALICE Technologies is a Menlo Park, California construction technology company that builds an AI-driven generative scheduling and construction optioneering platform. The product simulates millions of possible construction sequences for a project — varying crews, equipment, methods, and constraints — to find optimal schedules, accelerate timelines, recover delayed projects, and de-risk capital project delivery. ALICE's suite includes ALICE Optimize (generative scheduling from imported Primavera P6 or Microsoft Project schedules), ALICE Plan (a 2D visual planning canvas overlaid on drawings), ALICE Model (BIM-driven schedule generation from 3D models), and the Schedule Insights Agent (an LLM-powered conversational interface for analysing and recommending schedule changes, including automated DCMA 14-point schedule quality scoring). The platform is sold as SaaS to general contractors, owners and developers, and consultants working on industrial (data centres, energy, semiconductors),
  infrastructure (rail, highway, tunnels), and commercial projects, with reported impacts including up to 17% reduction in project duration and 14% labor cost savings. ALICE was founded in 2015 by René Morkos (Stanford PhD) and is backed by Merus Capital, Foundamental, Future Ventures, Lightspeed, Blackhorn Ventures, and Brick and Mortar; in 2026 it announced a formal alliance with McKinsey to deploy generative scheduling on capital projects. ALICE integrates by importing from Primavera P6, Primavera Cloud, Microsoft Project, and BIM/drawing formats, but does not publish a public developer API, SDK, or open-source repository — integration is delivered via the product's import/export surface and customer-success engagements.
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/alice-tech.png
layout: provider
modified: '2026-05-25'
name: ALICE Technologies
nav: Providers
network: true
overview: 'ALICE Technologies is profiled on the [APIs.io](https://apis.io/) network. Tagged areas include Construction, Construction Technology, Scheduling, Generative Scheduling, and Construction Optioneering.


  ALICE Technologies'' developer surface includes support, engineering blog, product news, YouTube channel, and 15 more developer resources.'
random_paper: 9
score:
  band: minimal
  composite: 8.3
  coverage:
    artifact_dirs: 3
    catalog_earned: 27.0
    catalog_earned_first_party: 0.0
    catalog_gap: 88.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 7.9
    commercial_clarity: 7.9
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 7.1
    discoverability: 50.0
    governance: 0.0
    operational_transparency: 2.6
  previous_composite: 8.3
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/alice-tech/refs/heads/main/screenshots/alice-tech-2026-06-20T171521.png
security:
- kind: domain-security
  name: Alice Tech Domain Security
  slug: alice-tech-domain-security
  summary_line: TLSv1.3 · HSTS · DNSSEC · DMARC
- kind: vulnerability-disclosure
  name: Alice Tech Vulnerability Disclosure
  slug: alice-tech-vulnerability-disclosure
  summary_line: security.txt · contact published
- kind: trust-center
  name: Alice Tech Trust Center
  slug: alice-tech-trust-center
  summary_line: SOC 2
slug: alice-tech
tags:
- Construction
- Construction Technology
- Scheduling
- Generative Scheduling
- Construction Optioneering
- Project Planning
- BIM
- Primavera P6
- Microsoft Project
- Schedule Optimization
- DCMA 14-Point
- Artificial Intelligence
- LLM
- Capital Projects
- Infrastructure
- Industrial Construction
website: https://www.alicetechnologies.com
---
