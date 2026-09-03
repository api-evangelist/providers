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
  scored_at: '2026-09-02'
api_count: 12
apis:
- description: Zowe is an open source software framework that delivers modern interfaces to interact with z/OS, including a CLI, a web UI (Application Framework), and REST APIs (API Mediation Layer) for jobs, datase
  name: Zowe
  slug: zowe
- description: Feilong is an open source z/VM cloud connector that exposes z/VM functions as REST APIs to accelerate z/VM adoption and enable integration with modern cloud automation tooling.
  name: Feilong
  slug: feilong
- description: Galasa is an open source deep integration test framework able to run tests across z/OS, distributed systems, and cloud platforms, with REST APIs for managing test runs and resources.
  name: Galasa
  slug: galasa
- description: Tessia automates the installation, configuration, and testing of Linux systems running on the IBM Z platform, exposing a REST API for managing systems, networks, and provisioning workflows.
  name: Tessia
  slug: tessia
- description: GenevaERS is a single-pass optimization engine for high-volume data extraction, transformation, and reporting on z/OS, used to consolidate large-scale mainframe analytics workloads.
  name: GenevaERS
  slug: genevaers
- description: COBOL Check is a unit testing framework for COBOL that enables test-driven development for mainframe code with assertion-based tests runnable from CI pipelines.
  name: COBOL Check
  slug: cobol-check
- description: zopen is a community-driven catalog and build framework that ports and packages popular open source tools for z/OS, expanding the open source tool surface available to mainframe developers.
  name: zopen Community
  slug: zopen-community
- description: Ambitus fosters a community focused on educating developers about open source technologies running on z/OS and Linux on Z, including curated tutorials and learning paths.
  name: Ambitus
  slug: ambitus
- description: CBT Tape is a long-running open library of free software distributions for IBM mainframe MVS, OS/390, and z/OS environments.
  name: CBT Tape
  slug: cbt-tape
- description: An open educational initiative offering structured COBOL learning materials alongside contemporary tooling such as VS Code, Zowe CLI, and Git for modern mainframe development workflows.
  name: COBOL Programming Course
  slug: cobol-programming-course
- description: Software Discovery Tool helps match developer requirements with available open source software tested on the IBM Z platform.
  name: Software Discovery Tool
  slug: software-discovery-tool
- description: Mainframe Open Education is a community for newcomers and experienced mainframe practitioners, sharing learning resources, mentoring guidance, and skills programs.
  name: Mainframe Open Education
  slug: mainframe-open-education
artifact_total: 16
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/openmainframeproject/feilong/issues
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/openmainframeproject/feilong/blob/master/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/openmainframeproject/feilong/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/openmainframeproject/feilong/blob/master/LICENSE
- group: auth
  title: ''
  type: DomainSecurity
  url: security/open-mainframe-project-domain-security.yml
- group: company
  title: ''
  type: LinkedIn
  url: https://www.linkedin.com/company/the-open-mainframe-project
- group: company
  title: ''
  type: Website
  url: https://www.openmainframeproject.org/
- group: other
  title: ''
  type: All Projects
  url: https://www.openmainframeproject.org/all-projects
- group: docs
  title: ''
  type: Documentation
  url: https://www.openmainframeproject.org/projects
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/openmainframeproject
- group: company
  title: ''
  type: Blog
  url: https://www.openmainframeproject.org/blog
- group: other
  title: ''
  type: Events
  url: https://www.openmainframeproject.org/events
- group: other
  title: ''
  type: Membership
  url: https://www.openmainframeproject.org/about/members
- group: other
  title: ''
  type: Linux Foundation
  url: https://www.linuxfoundation.org/projects/open-mainframe/
created: '2026-03-16'
description: The Open Mainframe Project is a Linux Foundation project encouraging the use of Linux-based operating systems and open source software on mainframe computers. Founded in 2015 with IBM, it hosts projects such as Zowe (modern interfaces for z/OS), Feilong (z/VM cloud connector), Galasa (testing), and a range of community programs that promote mainframe skills and open source on IBM Z and LinuxONE platforms.
finops:
- name: Open Mainframe Project Finops
  service_category: API
  slug: open-mainframe-project-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/open-mainframe-project.png
layout: provider
modified: '2026-04-28'
name: Open Mainframe Project
nav: Providers
network: true
overview: 'Open Mainframe Project publishes 12 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Cloud-Native, Education, Enterprise, IBM Z, and Linux Foundation.


  Open Mainframe Project''s developer surface includes documentation, engineering blog, and 12 more developer resources.'
plans:
- name: Open Mainframe Project Plans Pricing
  plan_count: 3
  slug: open-mainframe-project-plans-pricing
random_paper: 1
rate_limits:
- limit_count: 5
  name: Open Mainframe Project Rate Limits
  slug: open-mainframe-project-rate-limits
score:
  band: emerging
  composite: 13.6
  coverage:
    artifact_dirs: 6
    catalog_gap: 71.0
    catalog_max: 115.0
    note: Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider; it is our backlog, not their gap, and it is NOT subtracted from the composite above.
  delta: 0.0
  facets:
    access_clarity: 15.8
    commercial_clarity: 15.8
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 11.9
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 10.5
  open_source:
    applies: true
    score: 40.0
  previous_composite: 13.6
  regulatory:
    applies: true
    matched_via: tags
    regime: Education & Research
    regime_id: education
    score: 11.1
  schema_version: 0.18.0
  scored_at: '2026-09-02'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/open-mainframe-project/refs/heads/main/screenshots/open-mainframe-project-2026-06-20T190840.png
security:
- kind: domain-security
  name: Open Mainframe Project Domain Security
  slug: open-mainframe-project-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
slug: open-mainframe-project
tags:
- Cloud-Native
- Education
- Enterprise
- IBM Z
- Linux Foundation
- Linux on Z
- Mainframe
- Open-Source
- z/OS
- z/VM
website: https://www.openmainframeproject.org/
---
