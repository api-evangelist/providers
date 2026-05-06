---
aid: svn
name: Subversion
description: Apache Subversion (SVN) is a centralized version control system that tracks changes to files and directories over time. It supports atomic commits, directory versioning, cheap branching and tagging, merge tracking, and binary file handling. SVN is served over HTTP/HTTPS using the WebDAV/DeltaV protocol via mod_dav_svn, or over a custom protocol using svnserve.
type: Index
image: https://subversion.apache.org/images/svn-square.jpg
tags:
  - Apache
  - Open Source
  - Repository
  - Source Control
  - Svn
  - Version Control
  - Webdav
url: https://raw.githubusercontent.com/api-evangelist/svn/refs/heads/main/apis.yml
created: '2024-01-01'
modified: '2026-05-02'
specificationVersion: '0.19'
apis:
  - aid: svn:svn-webdav-http-api
    name: SVN WebDAV HTTP API
    description: Apache Subversion exposes repository operations over HTTP/HTTPS using the WebDAV/DeltaV protocol via the mod_dav_svn Apache module. Clients use OPTIONS, PROPFIND, GET, PUT, REPORT, MKACTIVITY, CHECKOUT, MERGE, COPY, DELETE, and PROPPATCH to perform version control operations including checkout, commit, update, log retrieval, and branching.
    humanURL: https://subversion.apache.org/docs/
    baseURL: https://svn.example.com/repos/
    tags:
      - Deltav
      - Repository
      - Version Control
      - Webdav
    properties:
      - type: Documentation
        url: https://subversion.apache.org/docs/
        x-type: Documentation
      - type: OpenAPI
        url: https://raw.githubusercontent.com/api-evangelist/svn/refs/heads/main/openapi/svn-webdav-openapi.yml
        x-type: OpenAPI
      - type: Book
        url: https://svnbook.red-bean.com/
        x-type: Documentation
      - type: Protocol
        url: https://svn.apache.org/repos/asf/subversion/trunk/notes/http-and-webdav/webdav-usage.html
        x-type: Documentation
    contact:
      - type: Email
        url: mailto:users@subversion.apache.org
      - type: Mailing List
        url: https://subversion.apache.org/mailing-lists.html
      - type: Issues
        url: https://issues.apache.org/jira/projects/SVN
  - aid: svn:svn-c-api
    name: SVN C Library API
    description: The Subversion C library provides the low-level API for building tools and integrations. It includes the libsvn_client, libsvn_ra, libsvn_wc, and libsvn_repos libraries for client operations, repository access, working copy management, and server-side repository access respectively.
    humanURL: https://subversion.apache.org/docs/api/latest/
    tags:
      - C Library
      - Integration
      - Library
    properties:
      - type: Documentation
        url: https://subversion.apache.org/docs/api/latest/
      - type: GitHub Repository
        url: https://github.com/apache/subversion
  - aid: svn:svn-python-bindings
    name: SVN Python Bindings
    description: Python bindings for Subversion C libraries, providing access to client and repository operations via pysvn and the official svn.client Python module.
    humanURL: https://pysvn.sourceforge.io/
    tags:
      - Python
      - SDK
    properties:
      - type: Documentation
        url: https://pysvn.sourceforge.io/Docs/pysvn_prog_guide.html
  - aid: svn:svn-java-bindings
    name: SVNKit Java Library
    description: SVNKit is a pure Java Subversion client library providing full access to Subversion repository and working copy data. Used by major IDE plugins including IntelliJ IDEA and Eclipse Subclipse.
    humanURL: https://svnkit.com/
    tags:
      - Java
      - SDK
    properties:
      - type: Documentation
        url: https://svnkit.com/index.html
common:
  - type: Getting Started
    url: https://subversion.apache.org/quick-start
  - type: Book
    url: https://svnbook.red-bean.com/
  - type: Downloads
    url: https://subversion.apache.org/download/
  - type: Security
    url: https://subversion.apache.org/security/
  - type: FAQ
    url: https://subversion.apache.org/faq.html
  - type: Community
    url: https://subversion.apache.org/mailing-lists.html
  - type: GitHub
    url: https://github.com/apache/subversion
  - type: License
    url: https://www.apache.org/licenses/LICENSE-2.0
  - type: Features
    url: https://subversion.apache.org/features.html
  - type: Package
    url: https://packages.apache.org/subversion
maintainers:
  - name: Apache Software Foundation
    email: dev@subversion.apache.org
    url: https://www.apache.org/
---
