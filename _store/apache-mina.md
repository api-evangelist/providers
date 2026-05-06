---
aid: apache-mina
name: Apache MINA
description: Apache MINA is a network application framework that helps develop high-performance and high-scalability network applications. It provides an abstract event-driven asynchronous API over various transports such as TCP/IP and UDP/IP via Java NIO. MINA includes sub-projects for SSH (SSHD), FTP (FtpServer), and XMPP (Vysper) protocols.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Async I/O
  - Java
  - Networking
  - NIO
  - Protocol Framework
  - SSH
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-mina/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-mina:apache-mina-core
    name: Apache MINA Core
    description: MINA Core provides a Java NIO-based API for building high-performance network applications with support for TCP and UDP protocols, an event-driven filter chain for protocol codecs, session management, and both client and server roles. Current version is 2.2.5.
    humanURL: https://mina.apache.org/mina-project/documentation.html
    tags:
      - Java
      - NIO
      - Networking
      - TCP
      - UDP
    properties:
      - type: Documentation
        url: https://mina.apache.org/mina-project/documentation.html
      - type: GettingStarted
        url: https://mina.apache.org/mina-project/userguide/user-guide-toc.html
      - type: SDK
        url: https://central.sonatype.com/artifact/org.apache.mina/mina-core
        title: Maven Central (Java)
      - type: GitHubRepository
        url: https://github.com/apache/mina
  - aid: apache-mina:apache-mina-sshd
    name: Apache MINA SSHD
    description: Apache MINA SSHD is a comprehensive Java library for client- and server-side SSH protocol implementation. It supports SCP, SFTP, port forwarding, key management, and various authentication methods. Current version is 2.17.1.
    humanURL: https://mina.apache.org/sshd-project/index.html
    tags:
      - Java
      - Security
      - SCP
      - SFTP
      - SSH
    properties:
      - type: Documentation
        url: https://mina.apache.org/sshd-project/index.html
      - type: SDK
        url: https://central.sonatype.com/artifact/org.apache.sshd/sshd-core
        title: Maven Central (Java)
      - type: GitHubRepository
        url: https://github.com/apache/mina-sshd
  - aid: apache-mina:apache-ftpserver
    name: Apache FtpServer
    description: Apache FtpServer is a 100% pure Java FTP server built on MINA. It is designed to be used as a complete and portable FTP server engine solution based on currently available open protocols. Current version is 1.2.1.
    humanURL: https://mina.apache.org/ftpserver-project/index.html
    tags:
      - FTP
      - Java
      - Server
    properties:
      - type: Documentation
        url: https://mina.apache.org/ftpserver-project/index.html
      - type: SDK
        url: https://central.sonatype.com/artifact/org.apache.ftpserver/ftpserver-core
        title: Maven Central (Java)
      - type: GitHubRepository
        url: https://github.com/apache/mina
common:
  - type: Portal
    url: https://mina.apache.org/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/mina
  - type: GitHubRepository
    url: https://github.com/apache/mina-sshd
  - type: GitHubRepository
    url: https://github.com/apache/mina-site
  - type: IssueTracker
    url: https://issues.apache.org/jira/browse/DIRMINA
  - type: MailingList
    url: https://mina.apache.org/mina-project/mailing-lists.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Features
    data:
      - name: Event-Driven Architecture
        description: Abstract event-driven asynchronous API enabling high-performance non-blocking I/O network application development.
      - name: Java NIO Foundation
        description: Built on Java NIO for scalable, non-blocking network I/O supporting thousands of concurrent connections.
      - name: Filter Chain
        description: Pluggable filter chain architecture for protocol codec, logging, compression, and security processing.
      - name: Multi-Transport Support
        description: Supports TCP/IP and UDP/IP transports with a unified programming model across both.
      - name: SSH Client and Server
        description: SSHD sub-project provides full SSH client and server implementation with SCP, SFTP, and port forwarding.
      - name: FTP Server
        description: FtpServer sub-project provides a complete, embeddable FTP server implementation built on MINA.
      - name: XMPP Server
        description: Vysper sub-project provides an extensible XMPP server implementation for instant messaging.
      - name: Session Management
        description: Comprehensive session lifecycle management with configurable timeouts, idle detection, and connection throttling.
  - type: UseCases
    data:
      - name: Custom Network Protocol Implementation
        description: Build custom client-server protocols over TCP/UDP using MINA's filter chain and codec framework.
      - name: SSH Automation and File Transfer
        description: Implement SSH automation, SFTP file transfer, and SCP operations using Apache MINA SSHD.
      - name: Embedded FTP Server
        description: Embed a fully functional FTP server within Java applications using Apache FtpServer.
      - name: High-Concurrency Network Services
        description: Build network services handling thousands of concurrent connections with minimal resource usage via NIO.
      - name: IoT Device Communication
        description: Implement lightweight IoT device communication protocols over TCP/UDP using MINA's framework.
  - type: Integrations
    data:
      - name: Spring Framework
        description: MINA integrates with the Spring Framework for dependency injection and application lifecycle management.
      - name: SLF4J and Logback
        description: Native SLF4J logging integration for structured logging across all MINA components.
      - name: Bouncy Castle
        description: Bouncy Castle cryptography library integration for SSH key management and cryptographic operations in SSHD.
      - name: Apache Karaf
        description: MINA components can be deployed as OSGi bundles in Apache Karaf container.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
