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
    asyncapi_events: false
    auth_clarity: false
    consent_identity: false
    dry_run_mode: false
    error_semantics: false
    idempotency: false
    mcp_server: false
    openapi_examples: false
    rate_limit_signal: documented
    spec_presence: false
    well_known_catalog: false
  schema_version: 0.2
  score: 3.2
  scored_at: '2026-07-28'
api_count: 3
apis:
- description: MINA Core provides a Java NIO-based API for building high-performance network applications with support for TCP and UDP protocols, an event-driven filter chain for protocol codecs, session management,
  name: Apache MINA Core
  slug: apache-mina-core
- description: Apache MINA SSHD is a comprehensive Java library for client- and server-side SSH protocol implementation. It supports SCP, SFTP, port forwarding, key management, and various authentication methods. Cu
  name: Apache MINA SSHD
  slug: apache-mina-sshd
- description: Apache FtpServer is a 100% pure Java FTP server built on MINA. It is designed to be used as a complete and portable FTP server engine solution based on currently available open protocols. Current vers
  name: Apache FtpServer
  slug: apache-ftpserver
artifact_total: 25
common:
- group: auth
  title: ''
  type: VulnerabilityDisclosure
  url: security/apache-mina-vulnerability-disclosure.yml
- group: auth
  title: ''
  type: DomainSecurity
  url: security/apache-mina-domain-security.yml
- group: start
  title: ''
  type: Portal
  url: https://mina.apache.org/
- group: build
  title: ''
  type: GitHubOrganization
  url: https://github.com/apache
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/mina
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/mina-sshd
- group: build
  title: ''
  type: GitHubRepository
  url: https://github.com/apache/mina-site
- group: operate
  title: ''
  type: IssueTracker
  url: https://issues.apache.org/jira/browse/DIRMINA
- group: other
  title: ''
  type: MailingList
  url: https://mina.apache.org/mina-project/mailing-lists.html
- group: commercial
  title: ''
  type: TermsOfService
  url: https://www.apache.org/licenses/LICENSE-2.0
created: '2026-03-16'
description: Apache MINA is a network application framework that helps develop high-performance and high-scalability network applications. It provides an abstract event-driven asynchronous API over various transports such as TCP/IP and UDP/IP via Java NIO. MINA includes sub-projects for SSH (SSHD), FTP (FtpServer), and XMPP (Vysper) protocols.
features:
- description: Abstract event-driven asynchronous API enabling high-performance non-blocking I/O network application development.
  name: Event-Driven Architecture
- description: Built on Java NIO for scalable, non-blocking network I/O supporting thousands of concurrent connections.
  name: Java NIO Foundation
- description: Pluggable filter chain architecture for protocol codec, logging, compression, and security processing.
  name: Filter Chain
- description: Supports TCP/IP and UDP/IP transports with a unified programming model across both.
  name: Multi-Transport Support
- description: SSHD sub-project provides full SSH client and server implementation with SCP, SFTP, and port forwarding.
  name: SSH Client and Server
- description: FtpServer sub-project provides a complete, embeddable FTP server implementation built on MINA.
  name: FTP Server
- description: Vysper sub-project provides an extensible XMPP server implementation for instant messaging.
  name: XMPP Server
- description: Comprehensive session lifecycle management with configurable timeouts, idle detection, and connection throttling.
  name: Session Management
finops:
- name: Apache Mina Finops
  service_category: API
  slug: apache-mina-finops
image: https://kinlane-images.s3.amazonaws.com/shared/apis-json/icons/apache-mina.png
integrations:
- description: MINA integrates with the Spring Framework for dependency injection and application lifecycle management.
  name: Spring Framework
- description: Native SLF4J logging integration for structured logging across all MINA components.
  name: SLF4J and Logback
- description: Bouncy Castle cryptography library integration for SSH key management and cryptographic operations in SSHD.
  name: Bouncy Castle
- description: MINA components can be deployed as OSGi bundles in Apache Karaf container.
  name: Apache Karaf
layout: provider
modified: '2026-04-19'
name: Apache MINA
nav: Providers
network: true
overview: 'Apache MINA publishes 3 APIs on the [APIs.io](https://apis.io/) network. Tagged areas include Async I/O, Java, Networking, NIO, and Protocol Framework.


  Apache MINA''s developer surface includes developer portal and 9 more developer resources.'
plans:
- name: Apache Mina Plans Pricing
  plan_count: 3
  slug: apache-mina-plans-pricing
random_paper: 36
rate_limits:
- limit_count: 5
  name: Apache Mina Rate Limits
  slug: apache-mina-rate-limits
score:
  band: emerging
  composite: 23.0
  delta: -2.3
  facets:
    commercial_clarity: 50.0
    contract_quality: 0.0
    developer_ergonomics: 8.7
    discoverability: 64.8
    governance: 0.0
    operational_transparency: 36.8
  previous_composite: 25.3
  schema_version: 0.6
  scored_at: '2026-07-28'
  trend: flat
screenshot: https://raw.githubusercontent.com/api-evangelist/apache-mina/refs/heads/main/screenshots/apache-mina-2026-06-20T172122.png
security:
- kind: domain-security
  name: Apache Mina Domain Security
  slug: apache-mina-domain-security
  summary_line: TLSv1.3 · HSTS · DMARC
- kind: vulnerability-disclosure
  name: Apache Mina Vulnerability Disclosure
  slug: apache-mina-vulnerability-disclosure
  summary_line: security.txt · contact published
slug: apache-mina
tags:
- Async I/O
- Java
- Networking
- NIO
- Protocol Framework
- SSH
use_cases:
- description: Build custom client-server protocols over TCP/UDP using MINA's filter chain and codec framework.
  name: Custom Network Protocol Implementation
- description: Implement SSH automation, SFTP file transfer, and SCP operations using Apache MINA SSHD.
  name: SSH Automation and File Transfer
- description: Embed a fully functional FTP server within Java applications using Apache FtpServer.
  name: Embedded FTP Server
- description: Build network services handling thousands of concurrent connections with minimal resource usage via NIO.
  name: High-Concurrency Network Services
- description: Implement lightweight IoT device communication protocols over TCP/UDP using MINA's framework.
  name: IoT Device Communication
website: https://mina.apache.org/
---
