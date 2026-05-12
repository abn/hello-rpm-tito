# GNU Hello RPM (tito)

A simple RPM package for testing tito-based RPM builder images. This is a tito-managed variant of [hello-rpm](https://github.com/abn/hello-rpm), based on the GNU Hello package from the [Fedora Packaging Guidelines](https://fedoraproject.org/wiki/Packaging:Guidelines).

## Prerequisites

- [tito](https://github.com/rpm-software-management/tito)

## Usage

### Tag a new release

```bash
# Bump version and tag (opens editor for changelog)
tito tag

# Tag without bumping (e.g. for the initial release)
tito tag --keep-version --no-auto-changelog
```

### Build

```bash
# Build SRPM from latest tag
tito build --srpm

# Build RPM from latest tag
tito build --rpm

# Test build from current HEAD (no tag required)
tito build --rpm --test
```

Output lands in `/tmp/tito/` by default.

## Layout

```
.tito/
  tito.props          # tito build/tag configuration
  packages/hello      # tracks current version and spec location
hello.spec            # RPM spec file
```
