# Security Policy

## Scope

This repository contains a static design-system specimen, design tokens, documentation, and local build/validation tooling. It does not operate a production service and should not contain credentials, user data, private application records, deployment configuration, or internal infrastructure details.

Security-relevant surfaces include:

- the token-to-CSS generator
- the release ZIP builder
- the static specimen
- the validation workflow
- repository automation

## Reporting

Report a vulnerability privately through GitHub's **Security** tab using a private vulnerability report or security advisory. Do not open a public issue containing credentials, personal information, private URLs, or exploit details.

Include:

- the affected file or workflow
- reproduction steps
- expected and actual behavior
- potential impact
- a suggested remediation, when available

## Secret exposure

If a credential or sensitive record is committed, revoke or rotate it immediately. Deleting the file or reverting the commit is not sufficient because the original data remains in Git history.

## Recommended repository controls

Repository administrators should enable these GitHub settings:

- require pull requests for changes to `main`
- require the `Validate` status check
- block force pushes and branch deletion
- enable secret scanning and push protection
- keep the default workflow token read-only unless a workflow has a documented need for additional permissions

These settings are enforced in GitHub rather than through files in this repository.

## Supported version

Only the latest version on the `main` branch is supported.
