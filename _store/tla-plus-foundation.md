---
aid: tla-plus-foundation
name: TLA Plus Foundation
description: The TLA+ Foundation is an independent nonprofit hosted by the Linux Foundation, dedicated to fostering the adoption of the TLA+ specification language in industry, academia, and education. Created by Leslie Lamport, TLA+ is a high-level formal specification language based on set theory and temporal logic for modeling concurrent and distributed systems. Inaugural members include Amazon Web Services (AWS) and Oracle. The Foundation funds research and development, maintains the TLC model checker, TLAPS proof system, and TLA+ Toolbox IDE, and coordinates community resources including the VS Code extension, CommunityModules, and formal verification examples. The current stable release is v1.7.4 (The Xenophanes release).
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Formal Methods
  - Linux Foundation
  - Specifications
  - Verification
  - Distributed Systems
  - Concurrency
created: '2026-03-16'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/tla-plus-foundation/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: tla-plus-foundation:tlc-model-checker
    name: TLC Model Checker
    description: TLC is the primary model checker for specifications written in TLA+. It can be run from the command line using tla2tools.jar or consumed as a Java dependency via Maven from central.sonatype.org. Requires Java 11+. The current stable release is v1.7.4 (The Xenophanes release) with pre-release v1.8.0 (The Clarke release) available.
    humanURL: https://github.com/tlaplus/tlaplus
    tags:
      - Model Checking
      - Formal Verification
      - Java
    properties:
      - type: Documentation
        url: https://tla.msr-inria.inria.fr/tlatoolbox/doc/model/executing-tlc.html
      - type: GitHubRepository
        url: https://github.com/tlaplus/tlaplus
  - aid: tla-plus-foundation:tlaps-proof-system
    name: TLAPS Proof System
    description: The TLA+ Proof Manager (TLAPS) is a proof system for TLA+ specifications, enabling formal mathematical proofs of system properties. It integrates with back-end provers and supports interactive proof development.
    humanURL: https://tla.msr-inria.inria.fr/tlaps/
    tags:
      - Proof System
      - Formal Verification
      - Mathematics
    properties:
      - type: Documentation
        url: https://tla.msr-inria.inria.fr/tlaps/
      - type: GitHubRepository
        url: https://github.com/tlaplus/tlapm
  - aid: tla-plus-foundation:tla-toolbox-ide
    name: TLA+ Toolbox IDE
    description: The TLA+ Toolbox is a full-featured IDE for writing TLA+ specifications, running TLC model checks, and managing proofs with TLAPS. Available as a standalone Eclipse-based application.
    humanURL: https://github.com/tlaplus/tlaplus
    tags:
      - IDE
      - Tooling
      - Development
    properties:
      - type: Documentation
        url: https://tla.msr-inria.inria.fr/tlatoolbox/doc/
      - type: GitHubRepository
        url: https://github.com/tlaplus/tlaplus
  - aid: tla-plus-foundation:vscode-tlaplus
    name: TLA+ VS Code Extension
    description: The official TLA+ extension for Visual Studio Code providing language support, syntax highlighting, TLC integration, and model checking from within the VS Code editor.
    humanURL: https://marketplace.visualstudio.com/items?itemName=alygin.vscode-tlaplus
    tags:
      - IDE
      - VS Code
      - Tooling
    properties:
      - type: Documentation
        url: https://github.com/tlaplus/vscode-tlaplus
      - type: GitHubRepository
        url: https://github.com/tlaplus/vscode-tlaplus
  - aid: tla-plus-foundation:community-modules
    name: TLA+ Community Modules
    description: A curated collection of TLA+ snippets, operators, and modules contributed by the TLA+ community, providing reusable formal specification components for common patterns in concurrent and distributed systems.
    humanURL: https://github.com/tlaplus/CommunityModules
    tags:
      - Community
      - Modules
      - Specifications
    properties:
      - type: Documentation
        url: https://github.com/tlaplus/CommunityModules
      - type: GitHubRepository
        url: https://github.com/tlaplus/CommunityModules
  - aid: tla-plus-foundation:tlaplus-examples
    name: TLA+ Specification Examples
    description: A collection of TLA+ specifications of varying complexity covering distributed algorithms, consensus protocols, concurrent data structures, and system models. Includes reference implementations for learning and validation.
    humanURL: https://github.com/tlaplus/Examples
    tags:
      - Examples
      - Specifications
      - Learning
    properties:
      - type: Documentation
        url: https://github.com/tlaplus/Examples
      - type: GitHubRepository
        url: https://github.com/tlaplus/Examples
common:
  - type: Website
    url: https://foundation.tlapl.us/
  - type: Documentation
    url: https://lamport.azurewebsites.net/tla/tla.html
  - type: GitHubOrganization
    url: https://github.com/tlaplus
  - type: Support
    url: mailto:support@tlapl.us
  - type: Features
    data:
      - name: TLC Model Checker
        description: Explicit-state model checker for TLA+ specifications supporting both exhaustive verification and simulation modes.
      - name: TLAPS Proof System
        description: Interactive proof manager for formally verifying TLA+ specifications against mathematical proofs.
      - name: TLA+ Toolbox IDE
        description: Eclipse-based IDE for writing, model-checking, and managing TLA+ specifications with TLAPS integration.
      - name: VS Code Extension
        description: Official Visual Studio Code extension providing TLA+ language support and TLC integration.
      - name: Community Modules
        description: Reusable TLA+ operator and module library contributed and maintained by the community.
      - name: Grant Program
        description: Foundation grants funding research and industry initiatives to advance TLA+ specification and tool adoption.
      - name: Maven Package Distribution
        description: TLA+ tools available as Maven Java dependency from central.sonatype.org for programmatic integration.
      - name: PlusPy Python Interpreter
        description: Python interpreter for executing TLA+ specifications, enabling Python-based formal modeling workflows.
  - type: UseCases
    data:
      - name: Distributed Algorithm Verification
        description: Model-check distributed consensus, replication, and coordination protocols against safety and liveness properties.
      - name: Concurrent System Specification
        description: Formally specify concurrent data structures, lock-free algorithms, and parallel systems using TLA+.
      - name: Protocol Design and Validation
        description: Use TLA+ to design and validate network protocols, database transactions, and API contracts before implementation.
      - name: Tooling Integration via Java API
        description: Embed TLC model checking in CI/CD pipelines or custom tools using the tla2tools Maven dependency.
      - name: Education and Training
        description: Use the TLA+ Toolbox, VS Code extension, and Leslie Lamport's video course to learn formal methods.
      - name: Safety and Liveness Proof
        description: Use TLAPS to produce machine-checked proofs of safety and liveness properties for critical systems.
  - type: Integrations
    data:
      - name: Amazon Web Services
        description: Founding member; AWS uses TLA+ for distributed systems design including DynamoDB and S3 protocols.
      - name: Oracle
        description: Founding member; uses TLA+ for database and distributed system specification.
      - name: Microsoft
        description: Early TLA+ adopter for Azure and distributed systems formal verification.
      - name: Visual Studio Code
        description: Official VS Code extension for TLA+ editing and model checking.
      - name: Maven Central
        description: TLA+ tools distributed as Java Maven dependency for programmatic integration.
      - name: Linux Foundation
        description: Parent organization hosting the TLA+ Foundation as an independent nonprofit project.
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
