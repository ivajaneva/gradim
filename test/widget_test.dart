import 'package:flutter/material.dart';
import 'package:flutter_test/flutter_test.dart';
import 'package:gradim/main.dart';

void main() {
  testWidgets('Gradim home page displays correctly', (tester) async {
    await tester.pumpWidget(const GradimApp());

    expect(find.text('Gradim'), findsWidgets);
    expect(
      find.text('Organizacija in spremljanje dela na gradbišču'),
      findsOneWidget,
    );
    expect(find.byIcon(Icons.construction), findsOneWidget);
  });
}