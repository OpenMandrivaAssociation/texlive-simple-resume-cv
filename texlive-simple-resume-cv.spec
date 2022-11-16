Name:		texlive-simple-resume-cv
Version:	43057
Release:	1
Summary:	Template for a simple resume or curriculum vitae (CV), in XeLaTeX
Group:		Publishing
URL:		http://www.ctan.org/tex-archive/macros/latex/contrib/simple-resume-cv
License:	pd
Source0:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simple-resume-cv.r%{version}.tar.xz
Source1:	http://mirrors.ctan.org/systems/texlive/tlnet/archive/simple-resume-cv.doc.r%{version}.tar.xz
BuildArch:	noarch
BuildRequires:	texlive-tlpkg
Requires(pre):	texlive-tlpkg
Requires(post):	texlive-kpathsea

%description
Template for a simple resume or curriculum vitae (CV), in
XeLaTeX. Simple template that can be further customized or
extended, with numerous examples.

%prep
%autosetup -p1 -c -a1

%build

%install
rm -rf tlpkg
mkdir -p %{buildroot}%{_texmfdistdir}
cp -a * %{buildroot}%{_texmfdistdir}

%files
%{_texmfdistdir}/tex/xelatex/simple-resume-cv
%doc %{_texmfdistdir}/doc/xelatex/simple-resume-cv

%post -p %{_sbindir}/texlive.post

%postun
[ "$1" -eq 0 ] && %{_sbindir}/texlive.post
