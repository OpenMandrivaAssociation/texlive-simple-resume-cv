%global tl_name simple-resume-cv
%global tl_revision 43057

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Template for a simple resume or curriculum vitae (CV), in XeLaTeX
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/macros/xetex/latex/simple-resume-cv
License:	pd
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simple-resume-cv.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/simple-resume-cv.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
Template for a simple resume or curriculum vitae (CV), in XeLaTeX.
Simple template that can be further customized or extended, with
numerous examples.

