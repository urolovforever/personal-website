import React from 'react';
import { FaGithub, FaLinkedin, FaTelegram, FaEnvelope, FaDownload } from 'react-icons/fa';

const HeroSection = () => {
  const socialLinks = [
    { icon: FaGithub, href: 'https://github.com/urolovforever', label: 'GitHub' },
    { icon: FaLinkedin, href: 'https://www.linkedin.com/in/nizomjonurolov', label: 'LinkedIn' },
    { icon: FaTelegram, href: 'tel:+998950393669', label: 'Phone' },
    { icon: FaEnvelope, href: 'mailto:nizomjonurolov24@gmail.com', label: 'Email' },
  ];

  return (
    <section
      id="home"
      className="min-h-screen flex items-center justify-center px-4 sm:px-6 lg:px-8 bg-gradient-to-br from-primary-50 to-white dark:from-gray-900 dark:to-gray-800 pt-16"
    >
      <div className="max-w-7xl mx-auto text-center animate-fade-in">
        {/* Profile Image */}
        <div className="mb-8 animate-slide-down">
          <div className="w-40 h-40 mx-auto rounded-full bg-gradient-to-br from-primary-400 to-primary-600 p-1 shadow-2xl">
            <div className="w-full h-full rounded-full bg-gray-200 dark:bg-gray-700 flex items-center justify-center text-6xl font-bold text-primary-600 dark:text-primary-400">
              NU
            </div>
          </div>
        </div>

        {/* Name & Title */}
        <h1 className="text-5xl md:text-7xl font-bold mb-4 animate-slide-up">
          <span className="bg-gradient-to-r from-primary-600 to-primary-400 bg-clip-text text-transparent">
            Nizomjon Urolov
          </span>
        </h1>

        <h2 className="text-2xl md:text-3xl text-gray-600 dark:text-gray-300 mb-6 animate-slide-up">
          Junior Web Developer | Cybersecurity Enthusiast
        </h2>

        {/* Tagline */}
        <p className="text-lg md:text-xl text-gray-600 dark:text-gray-400 max-w-2xl mx-auto mb-8 animate-fade-in">
          Passionate about building clean, responsive, and user-friendly websites.
          Currently strengthening cybersecurity skills to create secure and efficient web applications.
        </p>

        {/* Social Links */}
        <div className="flex justify-center space-x-4 mb-8 animate-slide-up">
          {socialLinks.map((social) => (
            <a
              key={social.label}
              href={social.href}
              target="_blank"
              rel="noopener noreferrer"
              className="p-3 rounded-full bg-white dark:bg-gray-800 shadow-md hover:shadow-xl transform hover:scale-110 transition-all duration-300 text-gray-700 dark:text-gray-300 hover:text-primary-600 dark:hover:text-primary-400"
              aria-label={social.label}
            >
              <social.icon className="w-6 h-6" />
            </a>
          ))}
        </div>

        {/* CTA Buttons */}
        <div className="flex flex-col sm:flex-row justify-center gap-4 animate-slide-up">
          <a
            href="/path-to-your-cv.pdf"
            download
            className="btn-primary inline-flex items-center justify-center gap-2"
          >
            <FaDownload className="w-4 h-4" />
            Download CV
          </a>
          <a
            href="#contact"
            onClick={(e) => {
              e.preventDefault();
              document.querySelector('#contact')?.scrollIntoView({ behavior: 'smooth' });
            }}
            className="btn-secondary inline-flex items-center justify-center gap-2"
          >
            <FaEnvelope className="w-4 h-4" />
            Contact Me
          </a>
        </div>

        {/* Scroll Indicator */}
        <div className="mt-16 animate-bounce">
          <a
            href="#about"
            onClick={(e) => {
              e.preventDefault();
              document.querySelector('#about')?.scrollIntoView({ behavior: 'smooth' });
            }}
            className="inline-block"
          >
            <svg
              className="w-6 h-6 text-primary-600 dark:text-primary-400"
              fill="none"
              strokeLinecap="round"
              strokeLinejoin="round"
              strokeWidth="2"
              viewBox="0 0 24 24"
              stroke="currentColor"
            >
              <path d="M19 14l-7 7m0 0l-7-7m7 7V3"></path>
            </svg>
          </a>
        </div>
      </div>
    </section>
  );
};

export default HeroSection;
