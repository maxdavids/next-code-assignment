import { NextResponse } from 'next/server';
import type { NextRequest } from 'next/server';

const publicRoutes = ['/login', '/signup'];

export function middleware(req: NextRequest) {
  /*
  const token = req.cookies.get('token'); // Assuming you store the JWT in cookies

  // Check if the current path is a public route
  const isPublicRoute = publicRoutes.some((route) => req.nextUrl.pathname.startsWith(route));

  if (isPublicRoute) {
    return NextResponse.next(); // Allow access to public routes
  }

  // If the token doesn't exist and the route is not public, redirect to login
  if (!token) {
    const loginUrl = new URL('/login', req.url);
    return NextResponse.redirect(loginUrl);
  }
  */

  // Proceed to the requested route if the token exists
  return NextResponse.next();
}

// Middleware should apply to all routes
export const config = {
  matcher: ['/tasks/:path*', '/dashboard/:path*'], // Add all protected routes
};
