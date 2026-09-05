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
  scored_at: '2026-09-04'
api_count: 2
apis:
- description: Maven provides a Java API for programmatic build execution, a Plugin API (Mojo) for extending build capabilities, a Repository API for artifact management via Maven Artifact Resolver, and the Wagon tr
  name: Apache Maven Core
  slug: apache-maven-core
- description: The Maven Central Repository (search.maven.org and central.sonatype.com) hosts millions of Java artifacts and provides a REST API and web interface for searching, browsing, and downloading dependencie
  name: Maven Central Repository API
  slug: maven-central-repository
artifact_total: 31
common:
- group: operate
  title: ''
  type: IssueTracker
  url: https://github.com/apache/maven/issues
- group: operate
  title: ''
  type: Releases
  url: https://github.com/apache/maven/releases
- group: auth
  title: ''
  type: SecurityPolicy
  url: https://github.com/apache/maven/blob/master/SECURITY.md
- group: build
  title: ''
  type: CodeOfConduct
  url: https://github.com/apache/.github/blob/main/.github/CODE_OF_CONDUCT.md
- group: docs
  title: ''
  type: ContributionGuide
  url: https://github.com/apache/maven/blob/master/CONTRIBUTING.md
- group: commercial
  title: ''
  type: License
  url: https://github.com/apache/maven/blob/master/LICENSE
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-maven-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-maven-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://maven.apache.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/maven
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/maven-resolver
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/maven-mvnd
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/maven-surefire
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/maven-enforcer
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/maven-assembly-plugin
- group: other
  title: ''
  type: Wiki
  url: https://cwiki.apache.org/confluence/display/MAVEN
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.apache.org/jira/projects/MNG/issues
- group: other
  title: ''
  type: MailingList
  url: https://maven.apache.org/mailing-lists.html
- group: company
  title: ''
  type: Blog
  url: https://maven.apache.org/news.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2026-03-16'
description: Apache Maven is a software project management and comprehension tool based on the concept of a project object model (POM). It provides a uniform build system, dependency management, project lifecycle, and a comprehensive plugin ecosystem for Java projects. Maven 4 is the current major version with the Maven Daemon for faster builds.
features:
- description: XML-based project descriptor that defines dependencies, build configuration, plugins, and project metadata in a declarative format.
  name: Project Object Model (POM)
- description: Automatic resolution and downloading of project dependencies and transitive dependencies from Maven Central and other repositories.
  name: Dependency Management
- description: Standardized build lifecycle with phases including validate, compile, test, package, verify, install, and deploy.
  name: Build Lifecycle
- description: Extensible plugin system (Mojo API) with hundreds of official and third-party plugins for code generation, testing, packaging, and deployment.
  name: Plugin Architecture
- description: Persistent daemon process that dramatically reduces build startup time by keeping the JVM and Maven warm between builds.
  name: Maven Daemon (mvnd)
- description: Ensures consistent Maven version usage across a project team without requiring separate Maven installation.
  name: Maven Wrapper
- description: Maven Artifact Resolver library provides programmatic API for artifact resolution, download, and local repository management.
  name: Artifact Resolver
- description: Support for building complex multi-module projects with inter-module dependency management and coordinated releases.
  name: Multi-Module Projects
- description: Latest major version with improved APIs, better performance, consumer POM support, and the Maven Upgrade Tool for migration.
  name: Maven 4
- description: Streamlined artifact publishing to Maven Central via Sonatype's publishing portal with automated checks.
  name: Central Repository Publishing
finops:
- name: Apache Maven Finops
  service_category: API
  slug: apache-maven-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-maven.png
integrations:
- description: Native Maven project support with POM editing, dependency management, and Maven tool window.
  name: IntelliJ IDEA
- description: Maven integration via the m2e plugin for POM-based project management within Eclipse IDE.
  name: Eclipse
- description: Jenkins Maven plugin for triggering and monitoring Maven builds in CI/CD pipelines.
  name: Jenkins
- description: Official GitHub Actions for caching Maven dependencies and running Maven builds in workflows.
  name: GitHub Actions
- description: Enterprise artifact repository manager fully compatible with Maven for hosting private artifact repositories.
  name: Sonatype Nexus
- description: Enterprise artifact repository with full Maven repository protocol support and build integration.
  name: JFrog Artifactory
- description: Tomcat Maven Plugin enables deploying web applications to Apache Tomcat directly from Maven builds.
  name: Apache Tomcat
- description: Maven plugins for building native images from Java applications using GraalVM Native Image.
  name: GraalVM
layout: provider
modified: '2026-04-19'
name: Apache Maven
nav: Providers
network: true
overview: 'Apache Maven publishes 2 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Build Tools, Dependency Management, Java, Project Management, and Maven.


  Apache Maven''s developer surface includes developer portal, engineering blog, and 19 more developer resources.'
plans:
- name: Apache Maven Plans Pricing
  plan_count: 3
  slug: apache-maven-plans-pricing
random_paper: 14
rate_limits:
- limit_count: 5
  name: Apache Maven Rate Limits
  slug: apache-maven-rate-limits
score:
  band: thin
  composite: 32.5
  coverage:
    artifact_dirs: 6
    catalog_earned: 41.0
    catalog_earned_first_party: 0.0
    catalog_gap: 74.0
    catalog_max: 115.0
    note: 'Disclosure, not a penalty. catalog_gap is rubric points API Evangelist could add with no action by this provider, and it is NOT subtracted from the composite above. It is our backlog EXCEPT where this provider already did the work: catalog_earned is how much of the class was satisfied at all, and catalog_earned_first_party how much of that came from artifacts the provider published rather than ones we generated (roadmap#221). catalog_earned_first_party is a FLOOR, not the whole share: only ~40 of the rubric''s 113 checks carry a provenance class at all, so a check we cannot attribute counts toward neither side. Read it as "at least this much was theirs", never as "the rest was ours".'
  delta: 0.0
  facets:
    access_clarity: 26.3
    commercial_clarity: 26.3
    contract_governance: 0.0
    contract_quality: 0.0
    developer_ergonomics: 45.2
    discoverability: 59.3
    governance: 0.0
    operational_transparency: 36.8
  open_source:
    applies: true
    score: 100.0
  previous_composite: 32.5
  schema_version: 0.18.3
  scored_at: '2026-09-04'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-maven/refs/heads/main/screenshots/apache-maven-2026-06-20T172120.png
security:
- kind: domain-security
  name: Apache Maven Domain Security
  slug: apache-maven-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Maven Vulnerability Disclosure
  slug: apache-maven-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-maven
tags:
- Build Tools
- Dependency Management
- Java
- Project Management
- Maven
use_cases:
- description: Automate compilation, testing, packaging, and deployment of Java projects with standardized build lifecycles.
  name: Java Project Build Automation
- description: Declare and automatically resolve project dependencies including transitive dependencies from Maven Central.
  name: Dependency Management
- description: Integrate Maven builds into CI/CD pipelines with reproducible builds via the Maven Wrapper and build cache extension.
  name: CI/CD Pipeline Integration
- description: Manage complex enterprise Java projects with dozens of interdependent modules and shared dependency management.
  name: Multi-Module Enterprise Builds
- description: Publish Java libraries and applications to Maven Central or private artifact repositories for team and public consumption.
  name: Artifact Publishing
- description: Develop custom Maven plugins using the Mojo API to extend build capabilities for specialized project needs.
  name: Plugin Development
website: https://maven.apache.org/
---
