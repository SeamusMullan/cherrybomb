# Frontend Components

This document outlines the general approach to frontend components in CherryBomb, focusing on reusability, maintainability, and consistency across the application. Specific components will often have their own detailed documentation if they are complex.

## Philosophy

- **Atomic Design Principles (loosely adopted)**: Components are thought of in terms of atoms (basic HTML elements like buttons, inputs), molecules (groups of atoms like a search form), organisms (more complex parts of an interface like a navigation bar or a content card), templates (page-level structures), and pages (specific instances of templates).

- **Reusability**: Components should be designed to be reusable across different parts of the application wherever possible.

- **Encapsulation**: Components should manage their own state and logic where appropriate, and expose a clear API through props.

- **Accessibility (A11y)**: Components should be built with accessibility in mind from the start, using semantic HTML and ARIA attributes where necessary.

- **Testability**: Components should be easy to test, both in isolation (unit tests) and as part of larger features (integration tests).

## Common Component Categories

### 1. UI Primitives / Atoms

These are the most basic building blocks of the UI.

- `Button`: Standard buttons with variations for primary, secondary, destructive actions, different sizes, and icon support.

- `Input`: Text inputs, textareas, number inputs, with validation and error states.

- `Select`: Dropdown selectors.

- `Checkbox` / `Radio`: Selection controls.

- `Label`: Text labels for form elements.

- `Icon`: Wrapper for SVG icons.

- `Typography` (e.g., `Heading`, `Text`, `Link`): Consistent text styling components.

- `Spinner` / `Loader`: Visual indicators for loading states.

### 2. Composite Components / Molecules

These components combine several primitive components to form more complex UI elements.

- `SearchBar`: Input field with a search button and possibly a clear button.

- `FormGroup`: Label, input, and error message combined.

- `Modal`: Dialog window for displaying information or requiring user interaction.

- `Card`: A container for displaying related information in a visually distinct block.

- `Notification` / `Toast`: For displaying temporary messages to the user.

- `Tabs`: For organizing content into different sections.

- `Pagination`: Controls for navigating through lists of items.

- `DatePicker`: For selecting dates.

### 3. Feature-Specific Components / Organisms

These are more complex components tailored to specific features of CherryBomb.

- `ContentPostCard`: Displays a summary of a social media post (thumbnail, caption, metrics).

- `MetricWidget`: Displays a single KPI with a title, value, and trend indicator (used on the Dashboard).

- `PlatformAccountItem`: Displays information about a connected social media account.

- `PredictionResultDisplay`: Shows the output of a prediction model for a piece of content.

- `CalendarEventItem`: Represents a scheduled post on the Content Calendar.

- `DataVisualizationWrapper`: A generic component that might wrap different chart types (bar, line, pie) with common controls like date pickers or filters.

### 4. Layout Components

These components define the structure of pages or sections.

- `PageLayout`: Standard layout for most pages, including header, sidebar, and content area.

- `Grid`: For arranging content in a grid system.

- `Sidebar`: Navigation sidebar.

- `Header`: Application header.

## Component Development Guidelines

- **Props**: Use clear and consistent naming for props. Define prop types using TypeScript interfaces.

- **State**: Manage component state locally with `useState` or `useReducer` for simple cases. For global or shared state, use Redux or Context API.

- **Styling**: Use CSS Modules, Styled-Components, or a utility-first CSS framework like Tailwind CSS to ensure styles are scoped and maintainable.

- **Storybook**: Consider using Storybook for developing and documenting UI components in isolation. This allows for easier testing and visual review of all component states.

- **Directory Structure**: Components are typically organized by feature or by type (e.g., `src/renderer/components/common/Button.tsx`, `src/renderer/features/dashboard/components/MetricWidget.tsx`).

## Example: Button Component

```typescript
// src/renderer/components/common/Button/Button.tsx
import React from 'react';
import './Button.css'; // Or using CSS-in-JS

interface ButtonProps extends React.ButtonHTMLAttributes<HTMLButtonElement> {
  variant?: 'primary' | 'secondary' | 'danger';
  size?: 'small' | 'medium' | 'large';
  isLoading?: boolean;
  leftIcon?: React.ReactNode;
  rightIcon?: React.ReactNode;
}

export const Button: React.FC<ButtonProps> = ({
  children,
  variant = 'primary',
  size = 'medium',
  isLoading = false,
  leftIcon,
  rightIcon,
  ...props
}) => {
  const SIZES = {
    small: 'py-1 px-2 text-sm',
    medium: 'py-2 px-4',
    large: 'py-3 px-6 text-lg',
  };

  const VARIANTS = {
    primary: 'bg-pink-600 text-white hover:bg-pink-700',
    secondary: 'bg-gray-200 text-gray-800 hover:bg-gray-300',
    danger: 'bg-red-600 text-white hover:bg-red-700',
  };

  return (
    <button
      className={`btn ${VARIANTS[variant]} ${SIZES[size]} ${isLoading ? 'opacity-75 cursor-not-allowed' : ''} flex items-center justify-center rounded focus:outline-none focus:ring-2 focus:ring-pink-500 focus:ring-opacity-50 transition ease-in-out duration-150`}
      disabled={isLoading || props.disabled}
      {...props}
    >
      {isLoading && <Spinner size="small" className="mr-2" />}
      {leftIcon && !isLoading && <span className="mr-2">{leftIcon}</span>}
      {children}
      {rightIcon && !isLoading && <span className="ml-2">{rightIcon}</span>}
    </button>
  );
};

// Dummy Spinner for example
const Spinner: React.FC<{ size: string, className?: string }> = ({ className }) => <div className={`animate-spin rounded-full h-5 w-5 border-t-2 border-b-2 border-white ${className}`}></div>;
```

This structured approach to frontend components helps in building a scalable and maintainable user interface for CherryBomb.
