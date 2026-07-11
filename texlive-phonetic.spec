%global tl_name phonetic
%global tl_revision 79618

Name:		texlive-%{tl_name}
Version:	%{tl_revision}
Release:	1
Summary:	Metafont Phonetic fonts, based on Computer Modern
Group:		Publishing
URL:		https://www.ctan.org/tex-archive/fonts/phonetic
License:	lppl1
Source0:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phonetic.r%{tl_revision}.tar.xz
Source1:	https://mirrors.ctan.org/systems/texlive/tlnet/archive/phonetic.doc.r%{tl_revision}.tar.xz
BuildArch:	noarch
BuildSystem:	texlive
Provides:	texlive(%{tl_name}) = %{tl_revision}

%description
The fonts are based on Computer Modern, and specified in Metafont.
Macros for the fonts' use are provided, both for LaTeX 2.09 and for
current LaTeX.

