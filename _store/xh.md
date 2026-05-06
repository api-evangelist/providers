---
aid: xh
name: Xh
description: xh is a friendly and fast command-line HTTP client written in Rust, designed as a modern, high-performance alternative to HTTPie. It reimplements HTTPie's request-item syntax and design with improved startup speed, HTTP/2 and HTTP/3 support, and availability as a single statically-linked binary. xh supports JSON and form data serialization, session management, authentication (basic, bearer, digest), SSL/TLS customization, multipart uploads, proxy configuration, and built-in curl command translation. Installable via Homebrew, Cargo, apt, pacman, and other package managers.
type: Index
image: https://kinlane-productions.s3.amazonaws.com/apis-json/apis-json-logo.jpg
tags:
  - CLI Tool
  - Command Line
  - Developer Tools
  - HTTP Client
  - Open Source
  - Rust
created: '2026-03-25'
modified: '2026-05-03'
url: https://raw.githubusercontent.com/api-evangelist/xh/refs/heads/main/apis.yml
specificationVersion: '0.19'
apis:
  - aid: xh:xh-cli
    name: Xh CLI
    description: xh is a friendly and fast command-line HTTP client written in Rust. It reimplements HTTPie's design with improved performance, HTTP/2 and HTTP/3 support, and a single statically-linked binary. Supports JSON and form data serialization, session persistence, basic/bearer/digest authentication, SSL/TLS certificate handling, proxy configuration, Unix socket connections, multipart file uploads, and built-in curl command translation. Uses HTTPie-compatible request-item syntax for setting headers, JSON fields, query parameters, and form data.
    humanURL: https://github.com/ducaale/xh
    tags:
      - CLI
      - HTTP
      - HTTP Client
      - Rust
      - Tool
    properties:
      - type: Documentation
        url: https://github.com/ducaale/xh#readme
      - type: GitHubRepository
        url: https://github.com/ducaale/xh
      - type: Releases
        url: https://github.com/ducaale/xh/releases
      - type: Changelog
        url: https://github.com/ducaale/xh/blob/master/CHANGELOG.md
      - type: ManPage
        url: https://github.com/ducaale/xh/blob/master/doc/xh.1
common:
  - type: Website
    url: https://github.com/ducaale/xh
  - type: GitHubRepository
    url: https://github.com/ducaale/xh
  - type: Documentation
    url: https://github.com/ducaale/xh#readme
  - type: Releases
    url: https://github.com/ducaale/xh/releases
  - type: Issues
    url: https://github.com/ducaale/xh/issues
  - type: License
    url: https://github.com/ducaale/xh/blob/master/LICENSE
  - type: Changelog
    url: https://github.com/ducaale/xh/blob/master/CHANGELOG.md
  - type: CargoPackage
    url: https://crates.io/crates/xh
maintainers:
  - FN: Kin Lane
    email: kin@apievangelist.com
---
