---
aid: open-mainframe-project
name: Open Mainframe Project
description: The Open Mainframe Project is a Linux Foundation project encouraging the use of Linux-based operating systems and open source software on mainframe computers. Founded in 2015 with IBM, it hosts projects such as Zowe (modern interfaces for z/OS), Feilong (z/VM cloud connector), Galasa (testing), and a range of community programs that promote mainframe skills and open source on IBM Z and LinuxONE platforms.
type: Index
position: Consumer
access: 3rd-Party
image: https://kinlane-productions2.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - Cloud Native
  - Education
  - Enterprise
  - IBM Z
  - Linux Foundation
  - Linux on Z
  - Mainframe
  - Open Source
  - z/OS
  - z/VM
created: '2026-03-16'
modified: '2026-04-28'
url: https://raw.githubusercontent.com/api-evangelist/open-mainframe-project/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: open-mainframe-project:zowe
    name: Zowe
    description: Zowe is an open source software framework that delivers modern interfaces to interact with z/OS, including a CLI, a web UI (Application Framework), and REST APIs (API Mediation Layer) for jobs, datasets, USS files, and system management.
    humanURL: https://www.zowe.org/
    tags:
      - API Mediation
      - CLI
      - Mainframe
      - REST APIs
      - z/OS
    properties:
      - type: Documentation
        url: https://docs.zowe.org/
      - type: GitHub Organization
        url: https://github.com/zowe
  - aid: open-mainframe-project:feilong
    name: Feilong
    description: Feilong is an open source z/VM cloud connector that exposes z/VM functions as REST APIs to accelerate z/VM adoption and enable integration with modern cloud automation tooling.
    humanURL: https://www.openmainframeproject.org/projects/feilong
    tags:
      - Cloud Connector
      - REST APIs
      - z/VM
    properties:
      - type: Documentation
        url: https://cloudlib4zvm.readthedocs.io/
      - type: GitHub Repository
        url: https://github.com/openmainframeproject/feilong
  - aid: open-mainframe-project:galasa
    name: Galasa
    description: Galasa is an open source deep integration test framework able to run tests across z/OS, distributed systems, and cloud platforms, with REST APIs for managing test runs and resources.
    humanURL: https://galasa.dev/
    tags:
      - Integration Testing
      - Mainframe
      - Test Automation
    properties:
      - type: Documentation
        url: https://galasa.dev/docs/
      - type: GitHub Organization
        url: https://github.com/galasa-dev
  - aid: open-mainframe-project:tessia
    name: Tessia
    description: Tessia automates the installation, configuration, and testing of Linux systems running on the IBM Z platform, exposing a REST API for managing systems, networks, and provisioning workflows.
    humanURL: https://gitlab.com/tessia-project
    tags:
      - Automation
      - Linux on Z
      - Provisioning
    properties:
      - type: Documentation
        url: https://gitlab.com/tessia-project/tessia/-/blob/master/README.md
      - type: GitLab Repository
        url: https://gitlab.com/tessia-project/tessia
  - aid: open-mainframe-project:genevaers
    name: GenevaERS
    description: GenevaERS is a single-pass optimization engine for high-volume data extraction, transformation, and reporting on z/OS, used to consolidate large-scale mainframe analytics workloads.
    humanURL: https://www.openmainframeproject.org/projects/genevaers
    tags:
      - Analytics
      - Data Extraction
      - z/OS
    properties:
      - type: Documentation
        url: https://genevaers.org/
      - type: GitHub Organization
        url: https://github.com/genevaers
  - aid: open-mainframe-project:cobol-check
    name: COBOL Check
    description: COBOL Check is a unit testing framework for COBOL that enables test-driven development for mainframe code with assertion-based tests runnable from CI pipelines.
    humanURL: https://www.openmainframeproject.org/projects/cobol-check
    tags:
      - COBOL
      - Testing
      - TDD
    properties:
      - type: GitHub Repository
        url: https://github.com/openmainframeproject/cobol-check
  - aid: open-mainframe-project:zopen-community
    name: zopen Community
    description: zopen is a community-driven catalog and build framework that ports and packages popular open source tools for z/OS, expanding the open source tool surface available to mainframe developers.
    humanURL: https://zopen.community/
    tags:
      - Open Source
      - Package Management
      - z/OS
    properties:
      - type: Documentation
        url: https://zopen.community/
      - type: GitHub Organization
        url: https://github.com/zopencommunity
  - aid: open-mainframe-project:ambitus
    name: Ambitus
    description: Ambitus fosters a community focused on educating developers about open source technologies running on z/OS and Linux on Z, including curated tutorials and learning paths.
    humanURL: https://www.openmainframeproject.org/projects/ambitus
    tags:
      - Community
      - Education
      - Linux on Z
      - z/OS
    properties:
      - type: GitHub Organization
        url: https://github.com/ambitus
  - aid: open-mainframe-project:cbt-tape
    name: CBT Tape
    description: CBT Tape is a long-running open library of free software distributions for IBM mainframe MVS, OS/390, and z/OS environments.
    humanURL: https://www.cbttape.org/
    tags:
      - Mainframe
      - MVS
      - Software Library
      - z/OS
    properties:
      - type: Documentation
        url: https://www.cbttape.org/
  - aid: open-mainframe-project:cobol-programming-course
    name: COBOL Programming Course
    description: An open educational initiative offering structured COBOL learning materials alongside contemporary tooling such as VS Code, Zowe CLI, and Git for modern mainframe development workflows.
    humanURL: https://github.com/openmainframeproject/cobol-programming-course
    tags:
      - COBOL
      - Education
      - Training
    properties:
      - type: GitHub Repository
        url: https://github.com/openmainframeproject/cobol-programming-course
  - aid: open-mainframe-project:software-discovery-tool
    name: Software Discovery Tool
    description: Software Discovery Tool helps match developer requirements with available open source software tested on the IBM Z platform.
    humanURL: https://www.openmainframeproject.org/projects/software-discovery-tool
    tags:
      - Discovery
      - IBM Z
      - Open Source
    properties:
      - type: GitHub Repository
        url: https://github.com/openmainframeproject/software-discovery-tool
  - aid: open-mainframe-project:mainframe-open-education
    name: Mainframe Open Education
    description: Mainframe Open Education is a community for newcomers and experienced mainframe practitioners, sharing learning resources, mentoring guidance, and skills programs.
    humanURL: https://www.openmainframeproject.org/projects/mainframe-open-education
    tags:
      - Community
      - Education
      - Mentorship
    properties:
      - type: Documentation
        url: https://www.openmainframeproject.org/projects/mainframe-open-education
common:
  - type: Website
    url: https://www.openmainframeproject.org/
  - type: All Projects
    url: https://www.openmainframeproject.org/all-projects
  - type: Documentation
    url: https://www.openmainframeproject.org/projects
  - type: GitHub Organization
    url: https://github.com/openmainframeproject
  - type: Blog
    url: https://www.openmainframeproject.org/blog
  - type: Events
    url: https://www.openmainframeproject.org/events
  - type: Membership
    url: https://www.openmainframeproject.org/about/members
  - type: Linux Foundation
    url: https://www.linuxfoundation.org/projects/open-mainframe/
maintainers:
  - FN: Kin Lane
    email: info@apievangelist.com
---
