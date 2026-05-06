---
aid: apache-maven
name: Apache Maven
description: Apache Maven is a software project management and comprehension tool based on the concept of a project object model (POM). It provides a uniform build system, dependency management, project lifecycle, and a comprehensive plugin ecosystem for Java projects. Maven 4 is the current major version with the Maven Daemon for faster builds.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Build Tool
  - Dependency Management
  - Java
  - Project Management
  - Maven
created: '2026-03-16'
modified: '2026-04-19'
url: https://raw.githubusercontent.com/api-evangelist/apache-maven/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: apache-maven:apache-maven-core
    name: Apache Maven Core
    description: Maven provides a Java API for programmatic build execution, a Plugin API (Mojo) for extending build capabilities, a Repository API for artifact management via Maven Artifact Resolver, and the Wagon transport API for repository access. Maven 4 introduces improved APIs and the Maven Upgrade Tool for migration.
    humanURL: https://maven.apache.org/guides/index.html
    tags:
      - Build
      - Java
      - Plugins
      - Project Object Model
    properties:
      - type: Documentation
        url: https://maven.apache.org/guides/index.html
      - type: GettingStarted
        url: https://maven.apache.org/install.html
      - type: APIReference
        url: https://maven.apache.org/ref/current/
      - type: SDK
        url: https://central.sonatype.com/artifact/org.apache.maven/maven-core
        title: Maven Central (Java)
      - type: GitHubRepository
        url: https://github.com/apache/maven
  - aid: apache-maven:maven-central-repository
    name: Maven Central Repository API
    description: The Maven Central Repository (search.maven.org and central.sonatype.com) hosts millions of Java artifacts and provides a REST API and web interface for searching, browsing, and downloading dependencies. It is the default artifact repository for Maven builds.
    humanURL: https://central.sonatype.com/
    tags:
      - Artifact Repository
      - Dependency Management
      - Package Registry
    properties:
      - type: Documentation
        url: https://central.sonatype.org/publish/
      - type: Portal
        url: https://central.sonatype.com/
      - type: APIReference
        url: https://central.sonatype.com/api-doc
common:
  - type: Portal
    url: https://maven.apache.org/
  - type: GitHubOrganization
    url: https://github.com/apache
  - type: GitHubRepository
    url: https://github.com/apache/maven
  - type: GitHubRepository
    url: https://github.com/apache/maven-resolver
  - type: GitHubRepository
    url: https://github.com/apache/maven-mvnd
  - type: GitHubRepository
    url: https://github.com/apache/maven-surefire
  - type: GitHubRepository
    url: https://github.com/apache/maven-enforcer
  - type: GitHubRepository
    url: https://github.com/apache/maven-assembly-plugin
  - type: Wiki
    url: https://cwiki.apache.org/confluence/display/MAVEN
  - type: IssueTracker
    url: https://issues.apache.org/jira/projects/MNG/issues
  - type: MailingList
    url: https://maven.apache.org/mailing-lists.html
  - type: Blog
    url: https://maven.apache.org/news.html
  - type: TermsOfService
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Features
    data:
      - name: Project Object Model (POM)
        description: XML-based project descriptor that defines dependencies, build configuration, plugins, and project metadata in a declarative format.
      - name: Dependency Management
        description: Automatic resolution and downloading of project dependencies and transitive dependencies from Maven Central and other repositories.
      - name: Build Lifecycle
        description: Standardized build lifecycle with phases including validate, compile, test, package, verify, install, and deploy.
      - name: Plugin Architecture
        description: Extensible plugin system (Mojo API) with hundreds of official and third-party plugins for code generation, testing, packaging, and deployment.
      - name: Maven Daemon (mvnd)
        description: Persistent daemon process that dramatically reduces build startup time by keeping the JVM and Maven warm between builds.
      - name: Maven Wrapper
        description: Ensures consistent Maven version usage across a project team without requiring separate Maven installation.
      - name: Artifact Resolver
        description: Maven Artifact Resolver library provides programmatic API for artifact resolution, download, and local repository management.
      - name: Multi-Module Projects
        description: Support for building complex multi-module projects with inter-module dependency management and coordinated releases.
      - name: Maven 4
        description: Latest major version with improved APIs, better performance, consumer POM support, and the Maven Upgrade Tool for migration.
      - name: Central Repository Publishing
        description: Streamlined artifact publishing to Maven Central via Sonatype's publishing portal with automated checks.
  - type: UseCases
    data:
      - name: Java Project Build Automation
        description: Automate compilation, testing, packaging, and deployment of Java projects with standardized build lifecycles.
      - name: Dependency Management
        description: Declare and automatically resolve project dependencies including transitive dependencies from Maven Central.
      - name: CI/CD Pipeline Integration
        description: Integrate Maven builds into CI/CD pipelines with reproducible builds via the Maven Wrapper and build cache extension.
      - name: Multi-Module Enterprise Builds
        description: Manage complex enterprise Java projects with dozens of interdependent modules and shared dependency management.
      - name: Artifact Publishing
        description: Publish Java libraries and applications to Maven Central or private artifact repositories for team and public consumption.
      - name: Plugin Development
        description: Develop custom Maven plugins using the Mojo API to extend build capabilities for specialized project needs.
  - type: Integrations
    data:
      - name: IntelliJ IDEA
        description: Native Maven project support with POM editing, dependency management, and Maven tool window.
      - name: Eclipse
        description: Maven integration via the m2e plugin for POM-based project management within Eclipse IDE.
      - name: Jenkins
        description: Jenkins Maven plugin for triggering and monitoring Maven builds in CI/CD pipelines.
      - name: GitHub Actions
        description: Official GitHub Actions for caching Maven dependencies and running Maven builds in workflows.
      - name: Sonatype Nexus
        description: Enterprise artifact repository manager fully compatible with Maven for hosting private artifact repositories.
      - name: JFrog Artifactory
        description: Enterprise artifact repository with full Maven repository protocol support and build integration.
      - name: Apache Tomcat
        description: Tomcat Maven Plugin enables deploying web applications to Apache Tomcat directly from Maven builds.
      - name: GraalVM
        description: Maven plugins for building native images from Java applications using GraalVM Native Image.
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
